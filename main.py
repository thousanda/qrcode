import qrcode

# テキストファイルからデータを読み込む
with open('data.txt', 'r') as file:
    data = file.read().strip()

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# データをQRコードに追加
qr.add_data(data)
qr.make(fit=True)

# QRコードを画像として生成
img = qr.make_image(fill_color="black", back_color="white")

# 画像を保存
img.save("generated_qrcode.png")
