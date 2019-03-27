# -*- coding:utf-8 -*-

import os
import shutil

nbi = "NBI"
normal = "normal"
pit = "pit"

def classify(root)
    root_list = os.listdir(root)
    for i in root_list:
        if i.endswith("DS_Store"):
            continue
        filename = os.listdir(os.path.join(root, i))
        for l in filename:
            path = os.path.join(root, i, l)
            if l.endswith("DS_Store"):
                continue
            elif l.endswith("normal_a.jpg"):
                shutil.copyfile(path, os.path.join(normal, "a", l))
            elif l.endswith("normal_b.jpg"):
                shutil.copyfile(path, os.path.join(normal, "b", l))
            elif l.endswith("normal_none.jpg"):
                shutil.copyfile(path, os.path.join(normal, "none", l))
            elif l.endswith("pit_a.jpg"):
                shutil.copyfile(path, os.path.join(pit, "a", l))
            elif l.endswith("pit_b.jpg"):
                shutil.copyfile(path, os.path.join(pit, "b", l))
            elif l.endswith("pit_none.jpg"):
                shutil.copyfile(path, os.path.join(pit, "none", l))
            elif l.endswith("NBI_a.jpg"):
                shutil.copyfile(path, os.path.join(nbi, "a", l))
            elif l.endswith("NBI_b.jpg"):
                shutil.copyfile(path, os.path.join(nbi, "b", l))
            elif l.endswith("NBI_none.jpg"):
                shutil.copyfile(path, os.path.join(nbi, "none", l))
            else:
                print(path)

if __name__ == "__main__":
    A = "polyp_A"
    B = "polyp_B"
    classify(A)
    classify(B)