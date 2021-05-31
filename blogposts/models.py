from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/')
	body = models.TextField()

	def __str__(self):
		return "{} - {}".format(self.title,self.pub_date)
	def summary(self):
		return self.body[:75]