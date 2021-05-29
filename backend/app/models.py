from django.db import models

# Create your models here.

class Post(models.Model):
	userName = models.CharField(max_length=200)
	file = models.FileField()
	visible = models.TextField(max_length=200)

	class Meta:
		db_table = "App-Post"
