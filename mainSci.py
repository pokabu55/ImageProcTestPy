# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt

def main():

    # 画像ファイル名の指定
    filename = "./data/IMG_0164.JPG"

    src = misc.imread(filename)

    plt.imshow(src)
    plt.show()

if __name__ == "__main__":
    main()
