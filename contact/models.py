from django.db import models

# Create your models here.
class contact(models.Model):
    name=  models.CharField(max_length=100,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200,verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=["-created_at"]