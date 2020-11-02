from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self): #function change the Post name "POstobj(1)" to first 50 character of text inside text field
        return self.text[:50]