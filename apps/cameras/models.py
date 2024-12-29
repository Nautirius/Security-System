from django.db import models
from django.db.models import UniqueConstraint
from ..buildings.models import Zone


class Camera(models.Model):
    label = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="cameras")
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()

    def __str__(self):
        return self.label


class CameraFeed(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('face', 'Face Image'),
        ('silhouette', 'Silhouette Image'),
    ]

    camera = models.OneToOneField(Camera, on_delete=models.CASCADE, related_name="feeds")
    image_path_face = models.ImageField(upload_to="camera_feeds/face/")
    image_path_silhouette = models.ImageField(upload_to="camera_feeds/silhouette/")
    date_uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['camera'], name='unique_feed_per_camera'),
        ]

    def __str__(self):
        return f"Feeds for {self.camera.label}"
