from pyzbar.pyzbar import decode
import cv2

# 画像ファイルの指定
image = cv2.imread("./data/src/Code39.jpg")

# QRコードの読取り
data = decode(image)

# コード内容を出力
print(data[0][0].decode('utf-8', 'ignore'))