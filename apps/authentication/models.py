from django.db import models
from django.contrib.auth.models import User
from pgvector.django import VectorField


# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=50, default="")
    street = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    zip_code = models.CharField(max_length=6, default="")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )


class UserImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('face', 'Face'),
        ('silhouette', 'Silhouette'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
    file_path = models.TextField()
    embedding = VectorField(null=True, blank=True) # TODO : EMBEDDINGS ??
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'image_type', 'file_path')