from django.db import models
from apps.buildings.models import Zone
from apps.authentication.models import UserProfile

class Permission(models.Model):
    label = models.CharField(max_length=255)
    zones = models.ManyToManyField(Zone, blank=True, null=True)
    users = models.ManyToManyField(UserProfile, blank=True, null=True)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label