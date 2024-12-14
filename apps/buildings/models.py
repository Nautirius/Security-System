from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_all_employees(self):
        from django.contrib.auth.models import User
        return list(User.objects.filter(memberships__company=self))

    def get_all_employees_with_roles(self):
        memberships = self.memberships.select_related('user')
        return [
            {'user': membership.user, 'role': membership.role} for membership in memberships
        ]

    def get_employees_by_role(self, role: str):
        from django.contrib.auth.models import User
        return list(
            User.objects.filter(memberships__company=self, memberships__role=role)
        )

    def assign_user(self, user_profile, role: str = "EMPLOYEE"):
        from apps.authentication.models import Membership
        Membership.objects.create(
            user_profile=user_profile,
            company=self,
            role=role
        )


class Building(models.Model):
    label = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="buildings")

    def __str__(self):
        return self.label


class Zone(models.Model):
    label = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="zones")

    def __str__(self):
        return f"{self.zone_id} ({self.building.label})"
