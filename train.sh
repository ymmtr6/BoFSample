for file in `find -maxdepth 1 -name 'g*-train.txt'` ; do svm-train -c 1 -g 0.001953125 $file; done
