from django.db import models

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=  1000)
    author =models.CharField(max_length=100, blank= False)
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)
class Meta:
    ordering = ['created']    
