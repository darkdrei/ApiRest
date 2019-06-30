from django.db import models
from status.querysets import StatusQuerySet


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self.db)