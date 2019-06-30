# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Api import settings
from status.managers import StatusManager
from status.utils import upload_update_image


class Status(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50] if self.content else '---- ----'

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural =  "Status posts"