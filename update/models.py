from django.core.serializers import serialize
from django.db import models
from django.conf import settings

import json
# Create your models here.
from django.http import JsonResponse
from django.views import View


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize2(self):
        qs = self
        print("LLego")
        return serialize('json', qs, fields=('user', 'content', 'image'))

    def serialize(self, text=None):
        print(' Query jajaja Esto es', text)
        qs = self
        array = []
        for obj in qs:
            struct = json.loads(obj.serialize(text))
            array.append(struct)
        return json.dumps(array)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self.db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self, fields=()):
        data = (serialize("json", [self], fields=('user', 'content', 'image')))
        struct = json.loads(data)
        print(struct)
        data = json.dumps(struct[0]['fields'])
        return data