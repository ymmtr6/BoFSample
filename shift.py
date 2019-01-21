# -*- coding:utf-8 -*-
import os.path
import argparse 
import cv2 
import pickle 

def load_dataset(dataset_path, mode):
    array = []
    for line in open(dataset_path):
        pair = line.strip().split()
        array.append([pair[1], load_image(pair[0], mode)])
    return array 

def load_image(image_path, mode):
    image = cv2.imread(image_path)
    return image

def output_image(img, keypoints, output_image_path):
    output = cv2.drawKeyPoints(img, keypoints, None, None, 4)
    cv2.imwrite(output_image_path, output)

def keypoint_info(keypoint):
    return keypoint.pt[0], keypoint.pt[1], keypoint.octave, keypoint.size, keypoint.angle, keypoint.response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)
    parser.add_argument("--output_pickle", "-p", default="SIFT_data.pickle", type=str)
    parser.add_argument("--output_image", "-i", default="", type=str)
    parser.add_argument("--color", "-c", default="bgr", type=str)
    parser.add_argument("--detector_types", "-d", default="ORB", type=str)
    parser.add_argument("--extractor_types", "-e", default="ORB", type=str)
    args = parser.parse_args()
    
    Supported_By_FeatureDetector_create = ["SIFT", "ORB"]
    Supported_By_DescriptorExtractor_create  = ["SIFT", "ORB"]

    if args.detector_types in Supported_By_DescriptorExtractor_create:
        # keypoint
        #detector = cv2.xfeatures2d.SIFT_create()
        detector = cv2.ORB_create()
    
    name, ext = os.path.splitext(args.input)
    if ext == ".txt":
        dataset = load_dataset(args.input, args.color)
    else:
        dataset = []
        dataset.append([0, load_image(args.input, args.color)])
    
    i = 0
    array = []
    for label, img in dataset:
        #keypoints, descriptors = detector.detectAndCompute(img)
        keypoints = detector.detect(img, None)
        descriptors = detector.compute(img, keypoints)

        if args.output_image != "":
            output_image(img, keypoints, args.output_image + "/" + str(i) + "_kp.png")
        
        array.append([label, descriptors])
        i = i + 1

    with open("train.txt", "w") as f:
        for label, keypoint in array:
            f.write("{} ".format(label))
            for i, key in enumerate(keypoint):
                f.write("{}:{} ".format(i, key))
            f.write("\n")

    
    #with open(args.output_pickle, "wb") as f:
    #    pickle.dump(array, f)
    
