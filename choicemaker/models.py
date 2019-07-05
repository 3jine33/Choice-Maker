from django.db import models

# Create your models here.
class Photo(models.Model) :
    title = models.CharField(max_length=200)
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')
    img4 = models.ImageField(upload_to='images/')

def __str__(self) :
    return self.title

