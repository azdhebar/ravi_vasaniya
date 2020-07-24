from django.urls import path
from gallary import views
urlpatterns = [
    path('',views.gallary,name="gallary")
]
