# -*- coding:utf-8 -*-

import os 
import random 
import argparse 

ROOT = "../data"
A = "a"
B = "b"
C = "none"

def write(filepath, array):
    with open(filepath, "w") as f:
        for path, number in array:
            f.write("{} {}\n".format(path, number))
    

def dist(method_root, target):
    """

    """
    train = []
    test = []

    a_list = os.path.join(ROOT, method_root, A)
    b_list = os.path.join(ROOT, method_root, B)
    c_list = os.path.join(ROOT, method_root, C)

    a_count = len(a_list)
    b_count = len(b_list)
    c_count = len(c_list)

    minimum = min(a_count, b_count, c_count)
    