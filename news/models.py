from django.db import models


class News(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')