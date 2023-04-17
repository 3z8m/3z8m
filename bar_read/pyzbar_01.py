from pyzbar.pyzbar import decode
from PIL import Image

# 画像ファイルの指定
image = "./data/src/Code39.jpg"

# バーコードの読取り
data = decode(Image.open(image))

# コード内容を出力
print(data[0][0].decode('utf-8', 'ignore'))