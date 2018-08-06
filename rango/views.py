from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# link = '<a href = "http://127.0.0.1:8000/rango/about/"> about page </a>'
	# return HttpResponse('Hey there partner ! -Rango' + link)
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	context_dict = {'author':'Christopher Camacho'}
	return render(request, 'rango/about.html', context = context_dict)