import qrcode as qrc


url = input("Enter url (or 'quit' to stop): ").strip()

name = input("Enter a name for this QR code: ").strip()
filepath = f"C:\\Users\\Raghav\\OneDrive\\Pictures\\Project_images\\{name}.png"

qr = qrc.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(filepath)

print(f"Your QR Code is generated! Saved as {name}.png :D")