# -*- coding:utf-8 -*-

import os

ROOT = "./data"
if __name__ == "__main__":
    array = []
    
    for img_path in os.listdir(os.path.join(ROOT, "gist")):
        array.append( [os.path.join(ROOT, "gist", img_path), 0])

    for img_path in os.listdir(os.path.join(ROOT, "other")):
        array.append( [os.path.join(ROOT, "other", img_path), 1])
    
    with open("label.txt", "w") as f:
        for path, number in array:
            f.write("{} {}\n".format(path, number))
