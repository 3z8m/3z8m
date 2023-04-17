'''
バーコード読み取り
https://note.nkmk.me/python-opencv-barcode/
'''

import cv2

img = cv2.imread('data/src/P1000484.jpg')

bd = cv2.barcode.BarcodeDetector()
# bd = cv2.barcode.BarcodeDetector('path/to/sr.prototxt', 'path/to/sr.caffemodel')

retval, decoded_info, decoded_type, points = bd.detectAndDecode(img)

print(retval)

# バーコードの値
print(decoded_info)

# 座標のタイプ
print(type(points))

# 4隅の座標
print(points)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

for s, p in zip(decoded_info, points):
    img = cv2.putText(img, s, p[1].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite('data/dst/barcode_opencv.jpg', img)