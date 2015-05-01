from django.contrib.auth.models import User

class UserInfo(models.Model):
	user = models.OneToOneField(User, related_name='info')
	description = models.TextField(null=True, blank=True)