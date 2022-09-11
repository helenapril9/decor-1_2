from decor_logger import path_log
import os
import sys

@path_log(sys.argv[0])
def calculator(a, b):
    return a + b

calculator(10, 20)
