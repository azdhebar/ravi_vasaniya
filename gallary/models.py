from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100,verbose_name="Category Name")
    contant = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"
        ordering=["-created_at"]

class Photo(models.Model):
    label=models.CharField(max_length=100,verbose_name="Label")
    photo = models.ImageField()
    category= models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering=["-created_at"]
