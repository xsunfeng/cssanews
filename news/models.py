from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	desc = models.CharField(max_length=200)
	thumb_url = models.CharField(max_length=200)
	content = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')