from distutils.command import upload
from django.db import models

# Create your models here.
class Event(models.Model):
    event_image = models.ImageField(upload_to="Event_images/")
    event_text = models.CharField(max_length=300)