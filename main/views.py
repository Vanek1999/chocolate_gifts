from django.shortcuts import render, redirect
from PIL import Image, ImageDraw, ImageFont
from .forms import Cart
from .models import Saves
from django.http import HttpResponse
import os

def index(request):
	#-----Обрабатываем форму или возвращаем страницу с формой-----
	if request.method == "POST":
		MyLoginForm = Cart(request.POST, request.FILES)
		if MyLoginForm.is_valid():
			#-----Сохраняем в бд-----
			Saves.objects.create(image = MyLoginForm.cleaned_data.get('image'), from_user = MyLoginForm.cleaned_data.get('from_user'), to_user = MyLoginForm.cleaned_data.get('to_user'), done_img = MyLoginForm.cleaned_data.get('image'))

			#-----Подготавлиеваем фотки-----
			im1 = Image.open('main/static/teamplate.jpg')
			im1 = im1.rotate(270, expand=True)
			im2 = Image.open('main/static/user_img/{}'.format(MyLoginForm.cleaned_data.get('image')))
			im2 = im2.resize((358, 500), Image.LANCZOS)

			#-----Пишем указанный текст юзером-----
			from_text = ImageDraw.Draw(im1)
			unicode_font = ImageFont.truetype("arial.ttf", 30)
			from_text.text((630, 850), 'От: {}'.format(MyLoginForm.cleaned_data.get('from_user')), fill=('#1C0606'), font=unicode_font)

			to_text = ImageDraw.Draw(im1)
			to_text.text((630, 950), 'Кому: {}'.format(MyLoginForm.cleaned_data.get('to_user')), fill=('#1C0606'), font=unicode_font)

			#-----Сохраняем-----
			im1.paste(im2, (617, 220))
			im1.save('main/static/done_img/{}.png'.format(MyLoginForm.cleaned_data.get('image')), quality=95)
			im1.close()
			im2.close()

			return redirect("download/{}".format(MyLoginForm.cleaned_data.get('image')))

	return render(request, 'index.html')

def download(request, file_name):
	#-----Забираем путь к фотке-----
	for i in Saves.objects.filter(done_img = "main/static/done_img/" + file_name):
		path = i.done_img

	#-----Возвращаем скачивание файла-----
	with open("{}".format(path) + ".png", "rb") as file:
		response = HttpResponse(file.read(), content_type="application/vnd.ms-excel")
		response['Content-Disposition'] = 'inline; filename=' + os.path.basename("{}".format(path))
	file.close()

	return response
