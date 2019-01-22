# -*- coding:utf-8 -*-
import argparse 
import warnings 
import pickle 
import numpy as np 
from sklearn.cluster import KMeans, MiniBatchKMeans

def make_dataset(n_clusters, labels, len_points, km_out, output):
    f2 = open(output, "w")
    point_first = 0
    for i in range(len(labels)):
        point_next_first = point_first + len_points[i]
        hg = histgram(n_clusters, km_out[point_first:point_next_first])
        point_first = point_next_first
        f2.write(str(labels[i]))
        for j in range(len(hg)):
            if hg[j] != 0:
                f2.write(" " + str(j+1) + ":" + str(hg[j]))
        f2.write("\n")
    f2.close()

def histgram(n_clusters, predicts):
    hg = [0] * n_clusters
    for pr in predicts:
        hg[pr] = hg[pr] + 1
    return hg

def array_structure_change(array):
    labels = []
    len_points = [] 
    km_in = [] 
    for im in array:
        labels.append(im[0])
        len_points.append(len(im[1]))
        for kp in im[1]:
            km_in.append(kp)
    return labels, len_points, km_in 

def main(input1, input2, output, output2):
    with open(input, "rb") as f_tr:
        array = pickle.load(f_tr)
    array = array_structure_change(array)

    km = MiniBatchKMeans(n_clusters=args.n_clusters, batch_size=1000, max_no_improvement=10)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        km.fit(array[2])
    
    km_out = km.predict(array[2])

    make_dataset(args.n_clusters, array[0], array[1], km_out, output)

    with open(input2, "rb") as f_te:
        array = pickle.load(f_te) 
    
    array = array_structure_change(array)

    km_out = km.predict(array[2])

    make_dataset(args.n_clusters, array[0], array[1], km_out, output2)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)
    parser.add_argument("input2", type=str)
    parser.add_argument("output", type=str)
    parser.add_argument("output2", type=str)
    parser.add_argument("--n_clusters", "-c", default=100, type=int)
    args = parser.parse_args()

    # main(args.input1, args.input2, args.output, args.output2)
