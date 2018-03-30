from django.db import models
from django.utils.six import python_2_unicode_compatible

    
class  Author(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name
    
class Style(models.Model):
    name =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Theme(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    style = models.ForeignKey('Style',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    news = models.TextField(blank=True)
    time = models.DateTimeField()
    theme = models.ForeignKey('Theme',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name