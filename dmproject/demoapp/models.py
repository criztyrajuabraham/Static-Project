from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class Teams(models.Model):
    name1 = models.CharField(max_length=45)
    img1 = models.ImageField(upload_to='teams')
    desc1 = models.TextField()

    def __str__(self):
        return self.name1