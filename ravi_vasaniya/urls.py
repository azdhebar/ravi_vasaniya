
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


admin.site.site_header = ("Administration")
admin.site.site_title = ("Administration")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('about/',include('about.urls')),
    path('gallary/',include('gallary.urls')),
    path('contact/',include('contact.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

