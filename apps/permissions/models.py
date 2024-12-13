from django.db import models
from apps.buildings.models import Zone
from apps.authentication.models import UserProfile

# Create your models here.
class Permission(models.Model):
    label = models.CharField(max_length=255)
    zones = models.ManyToManyField(Zone)
    users = models.ManyToManyField(UserProfile)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label