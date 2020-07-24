from django.shortcuts import render
from contact.models import contact

# Create your views here.
def contact_me(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            c = contact(name=name,email=email,subject=subject,message=message)
            c.save()
            success= "Thankyou!! We'll Contact You!"
            return render(request,'contact/pages/contact.html',{'success':success})
        except:
            error= "Something Went Wrong!!"
            return render(request,'contact/pages/contact.html',{'error':error})      
    else:      
        return render(request,'contact/pages/contact.html')