from django.contrib import admin
from home.models import Slider,SmallContact,SmallGallary
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here.


admin.site.register(SmallGallary)
admin.site.register(SmallContact)
admin.site.register(Slider)