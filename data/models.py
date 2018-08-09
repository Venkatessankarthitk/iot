from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rpm = models.CharField(max_length=400, null=True, blank=True)
    speed = models.CharField(max_length=400, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    # def __str__(self):
    #     return self.rpm

    # class Meta:
    #     unique_together = ("user", "type", "name")
    #     ordering = ['name']