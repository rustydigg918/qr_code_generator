import qrcode 

qr=qrcode.QRCode(version=1,
                                error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)
                    
qr.add_data("Pushkar Raj || Data Analyst@Guru & Jana Chartered Accountants\n\nGoodreads- https://www.goodreads.com/user/show/46427992-pushkar\n\nGithub- https://github.com/rustydigg918\n\nTwitter- https://twitter.com/rustydigg918")
qr.make(fit=True)

img = qr.make_image()
img.save("myname.png")