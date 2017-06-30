from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=300)
    permalink = models.CharField(max_length=200)
    content = models.TextField(null=True)


