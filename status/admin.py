# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from . import forms
# Register your models here.


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp', '__str__']
    form = forms.StatusForm

    """class Meta:
        model = models.Status"""

admin.site.register(models.Status, StatusAdmin)