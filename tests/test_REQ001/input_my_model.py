"""
Test MyModel
"""
import sys, os

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(os.path.dirname(current_directory))
sys.path.append(parent_directory)

from helper_my_model import MyModelSim, MyModel_Init
...

# Tests
def Test_My_Model(input):
    # Result array
    result = []

    # Initialize sub module
    MyModel_Init()

    # Check result
    for inp in input:
        res = MyModelSim(inp)
        result.append(res)
    return result
