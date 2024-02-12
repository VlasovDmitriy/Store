from django.shortcuts import render
# обработчики запросов = контроллеры = функции
# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')