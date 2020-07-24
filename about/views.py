from django.shortcuts import render
from .models import about
def about_bio(request):
    a1 = about.objects.latest('pk')
    return render(request,'about/pages/about.html',{'about':a1})
