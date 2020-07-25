from django.shortcuts import render
from gallary.models import  Category,Photo
# Create your views here.

def gallary(request):
    c = Category.objects.all()
    p = Photo.objects.all()
    return render(request,'gallary/pages/gallary.html',{'photos':p,'categories':c})

def gallary_category(request,id):
    try:
        cat = Category.objects.all()
        c = Category.objects.get(pk=id)
        p=Photo.objects.filter(category=c.pk)
        return render(request,'gallary/pages/gallary.html',{'photos':p,'category':c,'categories':cat})
    except:
        return redirect('gallary/')

