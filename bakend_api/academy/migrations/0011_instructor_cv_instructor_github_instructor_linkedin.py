# Generated by Django 5.0.3 on 2024-03-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0010_remove_course_image_remove_course_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='cv',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
