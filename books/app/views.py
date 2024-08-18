from django.shortcuts import render
from app.models import *

def homeview(request):
    a=booksmodel.objects.all()
    return render(request,'home.html',{'a':a})

def booksview(request):
    if request.method=='POST':
        b=request.POST.get('bname')
        p=request.POST.get('price')
        g=request.POST.get('genre')
        AID=request.POST.get('sno')
        im=request.FILES['imagen']
        if autermodel.objects.filter(id=AID).exists():
            a=autermodel.objects.get(id=AID)
            obj=booksmodel(title=b,price=p,genre=g,author=a,img=im)
            obj.save()
    return render(request,'books.html')

def authorview(request):
    if request.method=='POST':
        a=request.POST.get('aname')
        ag=request.POST.get('age')
        rat=request.POST.get('rate')
        if autermodel.objects.filter(name=a).exists():
            return render(request,'author.html')
        else:
            b=autermodel(name=a,age=ag,rating=rat)
            b.save()

    return render(request,'author.html')