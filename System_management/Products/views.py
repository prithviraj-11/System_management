from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here.
def addProduct(request):
    if(request.method=="GET"):
        return render(request,"addProduct.html",{})
    else:
        name=request.POST["name"]
        weight=request.POST["weight"]
        price=request.POST["price"]
        new_prod=Product(name=name,weight=weight,price=price)
        new_prod.save()
        return HttpResponse("Product added successfully")