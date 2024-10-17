# Example of array of user data type defined as class/structure
from ctypes import *
import numpy as np

# Must define the structure.

# Single point
class POINT(Structure):

    _fields_ = [("x", c_int),
                ("y", c_int),
                ]
    
class NUM(Structure):

    _fields_ = [("n", c_int),
                ]

# Multiple points
pts_all = POINT * 2
nums_all = NUM * 2

class POINTS(Structure):

    _fields_ = [("params1", pts_all),
                ("params2", nums_all)]
    
    def __init__(self, data_points, data_nums):
        self.params1 = pts_all(*data_points)
        self.params2 = nums_all(*data_nums)

# Instance of points/nums
point_list = [POINT() for i in range(2)]
#point_list = [POINT(2,3), POINT(4,5)]
point_list[0] = POINT(2,3)
nums_list = [NUM(1), NUM(2)]
points = POINTS(point_list, nums_list)

# Print points
print('List of points')
for pts1 in points.params1:
    print(pts1.x,pts1.y)

# Print nums
print('List of nums')
for nums1 in points.params2:
    print(nums1.n)
    