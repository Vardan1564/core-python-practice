import qrcode

data = "tel: 9510344614"

image="qrcode.jpeg"

makeqr =qrcode.make(data)

makeqr.save(image)

