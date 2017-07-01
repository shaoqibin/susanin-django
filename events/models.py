from django.db import models

# Create your models here.



class Guide(models.Model):
    name = models.CharField(max_length=300)
    nick = models.CharField(max_length=200, null=True)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='people', null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=300)
    permalink = models.CharField(max_length=200, null=True)
    short_desc = models.TextField(null=True, blank=True)
    long_desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='events', null=True, blank=True)
    tp_master_id = models.IntegerField(null=True)
    guides = models.ManyToManyField(Guide)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    text = models.TextField(null=True, blank=True)
    embed = models.TextField(null=True, blank=True)
    event_id = models.ForeignKey(Event, null=True)


class Review(models.Model):
    name = models.CharField(max_length=200)
    review = models.TextField(null=True, blank=True)
    event = models.ManyToManyField(Event, blank=True)
    def __str__(self):
        return self.name

