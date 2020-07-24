from django.db import models

# Create your models here.
class about(models.Model):
    name= models.CharField(max_length=100,verbose_name="Name")
    tag_line = models.CharField(max_length=200,verbose_name="TagLine")
    title1 = models.CharField(max_length=100,verbose_name="Title Of First Block")
    content1 = models.TextField(verbose_name="Content Of First Block")
    title2 = models.CharField(max_length=100,verbose_name="Title Of Second Block")
    content2 = models.TextField(verbose_name="Content Of Second Block")
    photo=  models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.name
    
    class Meta:
        ordering=["-created_at"]

    
    
    