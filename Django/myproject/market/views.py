from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'market/grocery_home.html')
def products(request):
    return render(request, 'market/products.html')
