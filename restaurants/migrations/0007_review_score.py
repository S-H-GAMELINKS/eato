# Generated by Django 3.2.6 on 2021-08-28 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_like_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
