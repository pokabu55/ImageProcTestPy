# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def showImage(src, usingOpenCV):

    if usingOpenCV == True:
        cv2.imshow("image", src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        plt.imshow(src)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show()


def main():

    # 画像ファイル名の指定
    filename = "./data/IMG_0164.JPG"

    # ファイルを開く
    src = cv2.imread(filename)

    # 処理する

    # OpenCV で表示する
    usingOpenCV = False
    showImage(src, usingOpenCV)

    # 保存する


if __name__ == "__main__":
    main()
