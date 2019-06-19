import random
from random import shuffle
from PIL import Image, ImageDraw, ImageFont


def burger_moment():
	borger = list('eeseburg')
	shuffle(borger)
	bruger = ''.join(borger)
	brugertje = f'Ch{bruger}er'
	
	img = Image.open("classes/burgertje.png")
	fnt = ImageFont.truetype('/snap/pycharm-community/132/jre64/lib/fonts/DroidSans-Bold.ttf', 40)
	d = ImageDraw.Draw(img)
	d.text((10,300), brugertje, font=fnt, fill=(0,0,0))
	d.text((11,301), brugertje, font=fnt, fill=(255,255,0))
	img.save('classes/borger.png')
	return 'smakelijk meneer :hamburger:  :hammer_pick:'
	



