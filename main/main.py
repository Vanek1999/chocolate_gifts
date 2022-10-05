from PIL import Image, ImageDraw, ImageFont


im1 = Image.open('teamplate.jpg')
im1 = im1.rotate(270, expand=True)
im2 = Image.open('i.png')
im2 = im2.resize((358, 500), Image.LANCZOS)


from_text = ImageDraw.Draw(im1)
unicode_font = ImageFont.truetype("arial.ttf", 30)
from_text.text((630, 850), 'От: python', fill=('#1C0606'), font=unicode_font)

to_text = ImageDraw.Draw(im1)
to_text.text((630, 950), 'Кому: Шуруповёрту', fill=('#1C0606'), font=unicode_font)

im1.paste(im2, (617, 220))
im1.save('fon_pillow_paste.png', quality=95)

im1.close()
im2.close()
