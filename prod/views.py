from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
import os
# Create your views here.

def index(request):
    return render(request,'index.html')

def save(request):
    if request.method=='POST':
        pro=Product()
        pro.name=request.POST['name']
        pro.price=request.POST['price']
        pro.subject=request.POST['subject']

        if len(request.FILES)!=0:
            pro.img=request.FILES['img']
        pro.save()
        messages.success(request, "Product Added successfully")
        return redirect('/')
    return render(request,'index.html')

def table(request):
    data = Product.objects.all()
    return render(request,'table.html',{'data':data})

def edit(request,pk):
    data=Product.objects.get(id=pk)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(data.img)>0:
                os.remove(data.img.path)
            data.img=request.FILES['img']
        data.name=request.POST['name']
        data.price=request.POST['price']
        data.subject=request.POST['subject']
        data.save()
        messages.success(request,'Product updated succesfully!')
        return redirect('table')
    return render(request,'edit.html',{'data':data})

