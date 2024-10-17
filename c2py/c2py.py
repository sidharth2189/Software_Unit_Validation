import sys
import os
import re
from pycparser import c_parser, c_ast
from ctypes import *

# Mapping of C types to ctypes equivalents
CTYPE_MAP = {
    'int': c_int,
    'short': c_short,
    'long': c_long,
    'char': c_char,
    'float': c_float,
    'double': c_double,
    
    # Add more mappings as needed
}

def parse_structs_from_header(header_file):
    structs = {}
    # Parse the header file
    parser = c_parser.CParser()
    with open(header_file, 'r') as f:
        content = f.read()
    # Remove C-style comments (/* ... */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'^\s*#.*?\n', '', content, flags=re.MULTILINE)
    # content = re.sub(r'\bextern\b\s*(?:(?:\w+\s+)+)?\w+\s*(?:\[\s*\d*\s*\])?\s*;', '', content)
    content = re.sub(r'\bextern\s+\S+\s+\S+\s*;', '', content)
    print(f"{header_file} ========")
    print(content)
    print("====================")
    try:
        ast = parser.parse(content, True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return structs;            

    # Extract structure definitions
    for node in ast.ext:
        if isinstance(node, c_ast.Decl) and isinstance(node.type, c_ast.Struct):
            struct_name = node.type.name
            fields = []
            for decl in node.type.decls:
                field_name = decl.name
                if isinstance(decl.type, c_ast.ArrayDecl):
                    array_size = None
                    if decl.type.dim:
                        array_size = int(decl.type.dim.value)
                        ctype = CTYPE_MAP.get(decl.type.type.type.names[0], None)
                        if(ctype != None):
                            ctype = ctype.__name__
                        else:
                            ctype = decl.type.type.type.names[0]
                        field_type = f'ARRAY({ctype},{array_size})'
                else:
                    ctype = CTYPE_MAP.get(decl.type.type.names[0], None)
                    if(ctype != None):
                        ctype = ctype.__name__
                    else:
                        ctype = decl.type.type.names[0]
                    field_type = ctype
                fields.append((field_name, field_type))
            structs[struct_name] = fields
    return structs

def generate_python_classes(structs):
    python_code = "from ctypes import *\n\n"
    for struct in structs:
        for struct_name, fields in struct.items():
            python_code += f"class {struct_name}(Structure):\n"
            python_code += "    _fields_ = [\n"
            for field_name, field_type in fields:
                # ctype = CTYPE_MAP.get(field_type, ctypes.c_void_p)
                python_code += f"        ('{field_name}', {field_type}),\n"
            python_code += "    ]\n\n"
    return python_code


def get_c_header_files(directory):
    header_files = []
    for file in os.listdir(directory):
        if file.endswith(".h"):
            header_files.append(os.path.join(directory, file))
    return header_files


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'
        
    python_code = []
    structs = []
    header_files = get_c_header_files(directory)
    for header_file in header_files:
        structs.append(parse_structs_from_header(header_file))
        
    python_code.append(generate_python_classes(structs))
    with open('_gen_py_c_structs.py', 'w') as f:
        for item in python_code:
            f.write('%s\n' % item)