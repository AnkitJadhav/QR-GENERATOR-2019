import qrcode

m = input("Paste your content here:")
n = input("Name your image here:")
img = qrcode.make(m)
img.save(n)