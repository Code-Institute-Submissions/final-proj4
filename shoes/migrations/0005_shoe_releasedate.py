# Generated by Django 3.1.4 on 2020-12-20 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_shoe_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]