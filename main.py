# -*- coding: utf-8 -*-

import cv2

def main():
    
    # 画像ファイル名の指定
    filename = "./data/IMG_0164.JPG"

    # ファイルを開く
    src = cv2.imread(filename)

    # 処理する

    # 表示する
    cv2.imshow("image", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存する


if __name__ == "__main__":
    main()
