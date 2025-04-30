from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def company(request):
    return render(request, 'home/company.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def map(request):
    return render(request, 'home/map.html')

def products(request):
    return render(request, 'home/products.html')

def category(request):
    return render(request, 'home/category.html')

def full(request):
    return render(request, 'home/fullproducts.html')

def basket(request):
    return render(request, 'home/basket.html')



