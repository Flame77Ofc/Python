import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
)

site = "https://flame77ofc.github.io/python-tutorial/"

qr.add_data(site)
qr.make(fit=True)

imagem = qr.make_image(fill_color="black", back_color="lightgray")

imagem.save("QR-code.png")
