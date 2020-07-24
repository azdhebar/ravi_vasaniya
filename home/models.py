from django.db import models

class Slider(models.Model):
    header=models.CharField(max_length=100,verbose_name="Header")
    content = models.TextField(verbose_name="Content")
    photo = models.ImageField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header

    class Meta:
        ordering=["-created_at"]

class SmallGallary(models.Model):
    name= models.CharField(max_length=100,verbose_name="Name")
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural= "Small Gallaries"
        ordering=["-created_at"]
    
class SmallContact(models.Model):
    header1 = models.CharField(verbose_name="Header First",max_length=100)
    header2 = models.CharField(verbose_name="Header Second",max_length=100)
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header1

    class Meta:
        ordering=["-created_at"]
    




