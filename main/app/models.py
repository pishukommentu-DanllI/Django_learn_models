from django.db import models

# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img_href = models.CharField(default='', max_length=500)
    id = models.IntegerField(primary_key=True)
    CheckBox = models.BooleanField(default=True)
    Selection = models.CharField(max_length=256)
