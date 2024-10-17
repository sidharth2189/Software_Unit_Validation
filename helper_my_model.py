"""
Define the C-variables and functions from the C-files that are needed in Python
"""
import sys, os
from interface_my_model import *

# Add relevant library path to directory
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname)
#filename = os.path.join(dirname, 'my_model_ert_rtw') # relative path to the generated library file/object
os.add_dll_directory(filename)


# Access library for generated code
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname)
os.add_dll_directory(filename)
lib_path = 'my_model.so'
try:
    MyModelLib = CDLL(lib_path)
except Exception as exc:
    print(f"The exception is : {exc}")

# Function to provide external input
def MyModelSim(input):
    """Call generated C code function/variable"""
    
    # Create local variable/structure equivalent of what is to be evaluated from C code
    value_U = aStruct.in_dll(MyModelLib, 'my_model_U')
    value_Y = aStruct.in_dll(MyModelLib, 'my_model_Y')

    # Assign input and run function from library
    value_U.x = input
    MyModelLib.my_model_step()

    return value_Y.x

# Function to initialize generated code (SwuAEBDecision)
def MyModel_Init():
    MyModelLib.my_model_initialize()
