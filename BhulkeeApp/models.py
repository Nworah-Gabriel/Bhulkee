from django.db import models
from uuid import uuid1
from datetime import datetime
# Create your models here.
class User(models.Model):
    """An OOP Database model that represents users in the platform"""

    id = models.UUIDField(primary_key=True, default=uuid1, editable=False, unique=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    secret_number = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    messages = models.ManyToManyField(to='Messages', blank=True)
    mails = models.ManyToManyField(to='MailLists', blank=True)

    def __str__(self):
        """A string representation of each instance"""
        return self.username


class Messages(models.Model):
    """An OOP Database model that represents messages sent by users in the platform"""

    id = models.CharField(max_length=40, primary_key=True, unique=True, default=uuid1)
    heading = models.CharField(max_length=500)
    body = models.TextField()
    date_pub = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.heading




class MailLists(models.Model):
    """An OOP Database model that represents mailing lists of each user in the platform"""

    id = models.CharField(max_length=40, primary_key=True, unique=True, default=uuid1)
    emails = models.CharField(max_length=200)
    def __str__(self):
        return self.emails