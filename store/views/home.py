from django.http import HttpResponse
from django.shortcuts import render, redirect

# import Models  
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
# Create your views here.


def index(request):
	#print(request.GET)
	productdata = None
	categoryID = request.GET.get('categoryid')
	#print(categoryID)
	if categoryID:
		productdata = Product.objects.filter(category=categoryID)
	else:
		productdata = Product.objects.all()
	
	categorydata = Category.objects.all()
	data = {'product': productdata,'category':categorydata}
	return render(request, 'index.html', data)



def login(request):
	return render(request, 'login.html')