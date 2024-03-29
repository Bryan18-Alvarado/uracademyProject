# Generated by Django 5.0.2 on 2024-02-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
            ],
        ),
    ]
