from django.db import models

# Create your models here.
class Topic(models.Model):
	sender_name = models.CharField(max_length = 10)
	topic_name = models.CharField(max_length = 10)	
