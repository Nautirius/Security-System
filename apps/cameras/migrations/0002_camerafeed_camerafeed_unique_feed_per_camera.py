# Generated by Django 4.2 on 2024-12-27 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path_face', models.ImageField(upload_to='camera_feeds/face/')),
                ('image_path_silhouette', models.ImageField(upload_to='camera_feeds/silhouette/')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('camera', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='cameras.camera')),
            ],
        ),
        migrations.AddConstraint(
            model_name='camerafeed',
            constraint=models.UniqueConstraint(fields=('camera',), name='unique_feed_per_camera'),
        ),
    ]
