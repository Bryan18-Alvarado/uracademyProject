# Generated by Django 5.0.3 on 2024-03-24 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0013_remove_orderitems_order_items_alter_course_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('detail', models.TextField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.course')),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.order')),
            ],
        ),
    ]
