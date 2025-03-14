# Generated by Django 4.2 on 2024-12-14 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("buildings", "0002_rename_company_id_building_company_and_more"),
        ("authentication", "0006_alter_userimage_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("EMPLOYEE", "Employee"),
                            ("ADMIN", "Admin"),
                            ("MANAGEMENT", "Management"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="buildings.company",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="authentication.userprofile",
                    ),
                ),
            ],
            options={
                "unique_together": {("user_profile", "company")},
            },
        ),
        migrations.AddField(
            model_name="userprofile",
            name="companies",
            field=models.ManyToManyField(
                related_name="users",
                through="authentication.Membership",
                to="buildings.company",
            ),
        ),
    ]
