import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

# 画像読込
src_img = Image.open('./data/src/Code39.jpg')

# 0.1倍〜2.0倍にリサイズ
rate = np.arange(0.1, 2.1, 0.1)
imgs = [src_img.resize((int(src_img.width * i), int(src_img.height * i)), Image.LANCZOS) for i in rate]

# コードスキャン
datas = [decode(img) for img in imgs]

# スキャン成功データのみをフィルタリング
*codes, = filter(lambda x: x, datas)

# 結果表示
if len(codes) > 0:
    # 一番初めにスキャン成功したものを表示
    code = codes[0]
    print(code[0][0].decode('utf8'))
else:
    print('INVARID')