# BoFSample

# 目的

Sift-SVMを用いて精度を確かめる．

## 環境構築

```
$ wget "http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+zip"
$ unzip libsvm-3.12.zip
$ cd libsvm-3.12
$ gmake
```

## コード実行

1. SIFT特徴量を抽出

```
python shift.py label.txt
```

label.txtは学習データとテストデータのラベル（特徴量の抽出は学習データとテストデータをまとめて使う）
コマンドでSIFT*_data.pickleが生成される．

2. k-meansクラスタリングして，SVMのコマンドの入力データに適した形式でtxtファイルを出力

```
python k-means.py train.pickle test.pickle train.txt test.txt -c 100
```

引数の-cは100は画像を100次元で表現したことを意味する．

3. 学習データをSVMに学習させる

```
svm-train -c 1 -g 0.001953125 train.txt
```

(http://manpages.ubuntu.com/manpages/cosmic/en/man1/svm-train.1.html)

このコマンドでtrain.txt.modelが生成される．

4. テストデータで性能評価

```
svm-predict test.txt train.txt.model class.txt -b 0
```

(http://manpages.ubuntu.com/manpages/cosmic/en/man1/svm-grid.1.html)