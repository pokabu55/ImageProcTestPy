# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def showImage(src, usingOpenCV, windowName):

    if usingOpenCV == True:
        cv2.imshow(windowName, src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        # src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        plt.imshow(src)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show()

def show2Images(src1, src1Name, src2, src2Name, usingOpenCV):

    if usingOpenCV == True:
        cv2.imshow(src1Name, src1)
        cv2.imshow(src2Name, src2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False

    return True

def averaging(src, rad=1):

    if rad <= 0:
        dst = src.copy()
        print("カーネルサイズが不適当なため、処理しません")
        return dst
    
    # カーネルサイズ
    kernelSize = rad*2 + 1

    # 入力画像サイズ
    imgH, imgW = src.shape[0], src.shape[1]

    # 出力画像配列
    # dst = np.zeros((imgH, imgW))
    dst = src.copy()

    # フィルタカーネル
    kernel = np.full((kernelSize,kernelSize), 1/(kernelSize*kernelSize))

    # 畳込み
    for y in range(rad, imgH-rad):
        for x in range(rad, imgW-rad):
            dst[y][x] = np.sum(src[y-rad:y+rad+1, x-rad:x+rad+1] * kernel)

    return dst

def main():

    # 画像ファイル名の指定
    filename = "./data/IMG_0164.JPG"

    # ファイルを開く
    # src = cv2.imread(filename)
    src = cv2.imread(filename, 0)

    # 処理する
    dst = averaging(src)

    # OpenCV or plt で表示する
    usingOpenCV = True #False
    show2Images(src, "src", dst, "dst", usingOpenCV)

    # 保存する


if __name__ == "__main__":
    main()
