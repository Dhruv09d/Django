from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE,) # many to one relationship
    body  = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # pk and id are interchangable in Django . acc to documentation
        # use id with get_absolute_url
        # here post-detail  require a PK so self.id is passed as argument
        return reverse('post-detail', args=[str(self.id)]) 