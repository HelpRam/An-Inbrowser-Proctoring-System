# Generated by Django 5.1.5 on 2025-02-01 08:22

import proctoring.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proctoring', '0004_cheatingevent_detected_objects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='timestamp',
            field=models.DateTimeField(default=proctoring.models.get_nepal_time),
        ),
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=proctoring.models.get_nepal_time),
        ),
    ]
