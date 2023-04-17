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

print(decoded_info)