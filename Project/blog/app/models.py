from django.db import models

class UserName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    file = models.FileField()
    visible = models.TextField()

    def __str__(self):
        return self.author