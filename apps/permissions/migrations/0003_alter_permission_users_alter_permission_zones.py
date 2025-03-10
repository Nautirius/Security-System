# Generated by Django 4.2 on 2024-12-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_rename_company_id_building_company_and_more'),
        ('authentication', '0007_membership_userprofile_companies'),
        ('permissions', '0002_alter_permission_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to='authentication.userprofile'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='zones',
            field=models.ManyToManyField(blank=True, null=True, to='buildings.zone'),
        ),
    ]
