# -*- coding:utf-8 -*-

import os
import random
import argparse

ROOT = "./data"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num", default=-1, type=int)
    parser.add_argument("--shuffle", "-s", action="store_false")
    parser.add_argument("--output", "-o", default="label.txt", type=str)
    args = parser.parse_args()

    array = []
    count = args.num

    gist_path = os.path.join(ROOT, "gist")
    other_path = os.path.join(ROOT, "other")

    if args.shuffle:
        random.shuffle(gist_path)
        random.shuffle(other_path)

    gist_list = [filename for filename in listdir(gist_path) if not filename.startswith('.')]
    other_list = [filename for filename in listdir(other_path) if not filename.startswith('.')]


    i = 0
    for img_path in gist_list:
        array.append( [os.path.join(ROOT, "gist", img_path), 0])
        if i == count - 1 and count != -1:
            break
        else:
            i+=1

    i = 0
    for img_path in other_list:
        array.append( [os.path.join(ROOT, "other", img_path), 1])
        if i == count - 1 and count != -1:
            break
        else:
            i+=1
    
    with open(args.output, "w") as f:
        for path, number in array:
            f.write("{} {}\n".format(path, number))
