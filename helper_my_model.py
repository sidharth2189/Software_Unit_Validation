"""
Define the C-variables and functions from the C-files that are needed in Python
"""
#from ctypes import c_double, c_int, CDLL
from ctypes import *
import sys
import os

# Must define the structure.
class aStruct(Structure):

    _fields_ = [("x", c_double)]

# Add relevant library path to directory
os.add_dll_directory("<complete local path to my_model_ert_rtw>")

# Access library for generated code
lib_path = 'my_model_%s.so' % (sys.platform)
try:
    MyModelLib = CDLL(lib_path)
except:
    print('OS %s not recognized' % (sys.platform))

# Set function/variable in library to set external input
# MyModel = MyModelLib.my_model_step
# MyModel.restype = None

# Function to provide external input
def MyModelSim(input):
    """Call generated C code function/variable"""
    
    # Create local variable/structure equivalent of what is to be evaluated from C code
    value_U = aStruct.in_dll(MyModelLib, 'my_model_U')
    value_Y = aStruct.in_dll(MyModelLib, 'my_model_Y')

    # Assign input and run function from library
    value_U.x = input
    MyModelLib.my_model_step()
    
    # Print I/O
    # print('Input is ' + str(value_U.x) + '\n')
    # print('Output is ' + str(value_Y.x) + '\n')

    return value_Y.x
