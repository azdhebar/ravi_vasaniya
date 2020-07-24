from django.shortcuts import render
from home.models import Slider,SmallContact,SmallGallary
# Create your views here.
def index(request):
    slider = Slider.objects.all()
    smallcontact= SmallContact.objects.latest('id')
    smallgallary =SmallGallary.objects.all()
    return render(request,'home/pages/index.html',{'sliders':slider,'scontact':smallcontact,'sgallaries':smallgallary})