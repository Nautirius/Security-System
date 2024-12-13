from django.db import models
from ..buildings.models import Zone


class Camera(models.Model):
    label = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="cameras")
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()

    def __str__(self):
        return self.label
