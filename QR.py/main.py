import qrcode

data  = input('Input whatever you want to: \n')

img = qrcode.make(data)
img.save(f'C:/Users/lnove/Desktop/PY Projects/QR.py/qr_codes/{data}.png')