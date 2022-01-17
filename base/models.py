from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# model name capital


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):

    name = models.CharField(max_length=200)
    # auto now add takes the date at the time of creation
    created = models.DateTimeField(auto_now_add=True)
    # auto now takes the date everytime its saved/edited
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    
    # room can have only one topic but many room can have same topic (many to one)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    host_user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    #arrange in ascending order  ordering=['updated','created']

    class Meta:
        # descending
        ordering=['-updated','-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # when parent is deleted this also gets deleted with cascade
    # when parent is deleted this gets null with SET_NULL
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # only 50 characters
        return self.body[0:50]

class extra(models.Model):
    task=models.CharField(max_length=100,null=False,blank=False)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.task
