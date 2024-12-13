from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
