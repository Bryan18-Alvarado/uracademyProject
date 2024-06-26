# Generated by Django 4.2.5 on 2024-06-06 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0027_course_demo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='cv',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
    ]
