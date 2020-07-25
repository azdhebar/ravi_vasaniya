from django.urls import path
from gallary import views
urlpatterns = [
    path('',views.gallary,name="gallary"),
    path('<int:id>/',views.gallary_category,name="category_gallay"),
]