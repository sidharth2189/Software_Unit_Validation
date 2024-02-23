import numpy as np
from helper_my_model import MyModelSim
...
input = np.array([1,2,3,4])
print('Input: ' + str(input) + '\n')
output = []
for inp in input:
    # Input to model
    res = MyModelSim(inp)

    # Add to output
    output.append(res)

    # Test output
    assert res == 2 * inp

print('Output: ' + str(output))