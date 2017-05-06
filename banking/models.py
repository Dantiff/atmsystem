from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='imgs', blank=True)

    def __unicode__(self):
            return self.user.username

class Account(models.Model):
    acc_owner = models.ForeignKey('auth.User')
    acc_name = models.CharField(max_length=200)
    acc_number = models.BigIntegerField()
    acc_balance = models.BigIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    remove_date = models.DateTimeField(blank=True, null=True)

    def remove(self):
        self.remove_date = timezone.now()
        self.save()

    def __str__(self):
        return self.acc_name
