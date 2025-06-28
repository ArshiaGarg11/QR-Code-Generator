import qrcode

data = input("Enter the text or URL to generate QR code: ")

qr = qrcode.make(data)


filename = "qr_code.png"
qr.save(filename)

print(f"QR code generated and saved as {filename}")
