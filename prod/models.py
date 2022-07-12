from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    price=models.CharField(max_length=8,null=True)
    subject=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
