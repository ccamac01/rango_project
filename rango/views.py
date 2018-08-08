from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
	# link = '<a href = "http://127.0.0.1:8000/rango/about/"> about page </a>'
	# return HttpResponse('Hey there partner ! -Rango' + link)
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]

	context_dict = {'categories':category_list, 'pages':page_list}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	context_dict = {'author':'Christopher Camacho'}
	return render(request, 'rango/about.html', context = context_dict)

def show_category(request, category_name_slug):
	context_dict = {}


	try:
		category = Category.objects.get(slug = category_name_slug)

		# Note that filter() will return a list of page objects or an empty list
		pages = Page.objects.filter(category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category

	except Category.DoesNotExist:
		context_dict['pages'] = None
		context_dict['category'] = None

	return render(request, 'rango/category.html', context_dict)

def add_category(request):
	form = CategoryForm()
	if (request.method == 'POST'):
		form = CategoryForm(request.POST)

		if (form.is_valid()):
			# save the form if it is valid
			form.save(commit = True)

			# redirect the user to the homepage
			return index(request)

		else:
			print(form.errors)
	return render(request, 'rango/add_category.html', {'form':form})























