from django.shortcuts import render
from urllib import request
from django.views import View
from . models import Product
from django.db.models import Count


# Create your views here.
def main(request):
    contex = {}
    return render(request,'store/main.html', contex)

def cart(request):
    contex = {}
    return render(request,'store/cart.html', contex)

def store(request):
    contex = {}
    return render(request,'store/store.html', contex)

# def category(request):
#     contex = {}
#     return render(request,'store/category.html', contex)
class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,"store/category.html",locals())
    

    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk = pk)
        return render(request, "store/productdetail.html",locals())
 
def about(request):
    contex = {}
    return render(request,'store/about.html', contex)

def contact(request):
    contex = {}
    return render(request,'store/contact.html', contex)
