from django.shortcuts import render
from gallary.models import  Category,Photo
# Create your views here.

def gallary(request):
    c = Category.objects.all()
    p = Photo.objects.all()
    return render(request,'gallary/pages/gallary.html',{'photos':p,'categories':c})