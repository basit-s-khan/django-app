from django.db import models

# Create your models here.

class person(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    joined_date = models.DateField(null = True)
    slug = models.SlugField(default="", null=False)
    
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"