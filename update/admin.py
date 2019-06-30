from django.contrib import admin
from .models import Update
from .forms import StatusForm
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']

    class Meta:
        model = Update

admin.site.register(Update, StatusAdmin)
