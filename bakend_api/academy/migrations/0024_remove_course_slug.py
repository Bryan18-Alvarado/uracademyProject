# Generated by Django 5.0.6 on 2024-05-24 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0023_categorycourse_image_coursesimages_categorycourse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
    ]
