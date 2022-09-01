import qrcode
txt = input('Enter your text: ')
adr = input('Enter the address: ')
Qr = qrcode.make(txt + '\n' + adr)
Qr.save('qr1.jpg')