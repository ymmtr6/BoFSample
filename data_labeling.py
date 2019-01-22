# -*- coding:utf-8 -*-

import os
import random
import argparse

ROOT = "./data"

def write(filepath, array):
    with open(filepath, "w"):
        for path, number in array:
            f.write("{} {}\n".format(path, number))

def dist(gist_list, other_list, target):
    """
    """
    train = []
    test = []
    for img_path in gist_list:
        p = os.path.join(ROOT, "gist", img_path)
        if img_path.startswith(target):
            test.append( [p, 0])
        else:
            train.append( [p, 0] )

    for img_path in other_list:
        p = os.path.join(ROOT, "other", img_path)
        if img_path.startswith(target):
            test.append( [p, 0])
        else:
            train.append([p, 0])
    
    with open("{}-{}train.txt".format(args.output, target), "w") as f:
        for path, number in train:
            f.write("{} {}\n".format(path, number))

    with open("{}-{}test.txt".format(args.output, target), "w") as f:
        for path, number in test:
            f.write("{} {}\n".format(path, number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", default="label", type=str)
    args = parser.parse_args()

    gist_path = os.path.join(ROOT, "gist")
    other_path = os.path.join(ROOT, "other")

    gist_list = [filename for filename in os.listdir(gist_path) if not filename.startswith('.')]
    other_list = [filename for filename in os.listdir(other_path) if not filename.startswith('.')]

    targets = []
    for i in range(32):
        targets.append("g{}-".format(i+1))
    for i in range(11):
        targets.append("o{}-".format(i+1))
    
    for target in targets:
        dist(gist_list, other_list, target)

    
    
