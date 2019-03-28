# -*- coding:utf-8 -*-

import os 
import random 
import argparse 
from os.path import join

ROOT = "../data"
A = "a"
B = "b"
C = "none"

def write(filepath, array):
    with open(filepath, "w") as f:
        for path, number in array:
            f.write("{} {}\n".format(path, number))
    

def dist(method_root):
    """

    """
    a_path = join(ROOT, method_root, A)
    b_path = join(ROOT, method_root, B)
    c_path = join(ROOT, method_root, C)
    a_list = os.listdir(a_path)
    b_list = os.listdir(b_path)
    c_list = os.listdir(c_path)
    random.shuffle(a_list)
    random.shuffle(b_list)
    random.shuffle(c_list)
    a_count = len(a_list)
    b_count = len(b_list)
    c_count = len(c_list)

    minimum = min(a_count, b_count, c_count)
    
    a_subset = []
    b_subset = []
    c_subset = []
    for i in range(10):
        a_l = []
        b_l = []
        c_l = []
        for _ in range(minimum / 10):
            a_l.append(join(a_path, a_list.pop(0)))
            b_l.append(join(b_path, b_list.pop(0)))
            c_l.append(join(c_path, a_list.pop(0)))
        a_subset.append(a_l) 
        b_subset.append(b_l) 
        c_subset.append(c_l)
    
    return a_subset, b_subset, c_subset

def labeling(method, k=10):
    a_sub, b_sub, c_sub = dist(method)
    for i in range(10):
        train = []
        test = []
        
        for j in range(10):        
            for a, b, c in zip(a_sub[j], b_sub[j], c_sub[j]):
                if i != j:
                    train.append([a, 0])
                    train.append([b, 1])
                    train.append([c, 2])
                else:
                    test.append([a, 0])
                    test.append([b, 1])
                    test.append([c, 2])
        
        write("{}-{}.train.text".format(method, i) target)
        write("{}-{}.test.txt".format(method, i), test)

if __name__ == "__main__":
    labeling("NBI")