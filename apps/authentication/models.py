from django.db import models
from django.contrib.auth.models import User
from pgvector.django import VectorField

from apps.buildings.models import Company


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
    companies = models.ManyToManyField(
        Company,
        through='Membership',
        related_name='users'
    )

    def get_all_companies(self):
        return list(self.companies.all())

    def get_all_companies_by_role(self, role: str):
        return list(self.companies.filter(memberships__role=role))

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


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


class Membership(models.Model):
    ROLE_CHOICES = [
        ('EMPLOYEE', 'Employee'),
        ('ADMIN', 'Admin'),
        ('MANAGEMENT', 'Management'),
    ]

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'company')  # Zapobiega duplikatom

    def __str__(self):
        return f"{self.user_profile.user.username} in {self.company.name} as {self.role}"