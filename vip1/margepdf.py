# import py
# import os

# merger=PfdWriter()
# file=[file for file in os.listdir()if file.endswith(".pdf")]

# for pdf in file :
#     merger.append(pdf)
# merger.write("my .pfd")
# merger.close()
import qrcode

data="Khirasra, Gujarat 360021"

image="qrcode.jpeg"

makeqr=qrcode.make(data)

makeqr.save(image)