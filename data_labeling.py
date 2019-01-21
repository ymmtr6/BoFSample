# -*- coding:utf-8 -*-

import os
import random

ROOT = "./data"
if __name__ == "__main__":
    array = []
    count = 1000
    
    i = 0

    gist_path = os.listdir(os.path.join(ROOT, "gist"))
    random.shuffle(gist_path)

    other_path = os.listdir(os.path.join(ROOT, "gist"))
    random.shuffle(other_path)
    
    for img_path in gist_path:
        array.append( [os.path.join(ROOT, "gist", img_path), 0])
        if i == count - 1:
            break
        else:
            i+=1

    i = 0
    for img_path in other_path:
        array.append( [os.path.join(ROOT, "other", img_path), 1])
        if i == count - 1:
            break
        else:
            i+=1
    
    with open("label.txt", "w") as f:
        for path, number in array:
            f.write("{} {}\n".format(path, number))
