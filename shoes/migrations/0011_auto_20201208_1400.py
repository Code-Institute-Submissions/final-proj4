# Generated by Django 3.1.4 on 2020-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0010_auto_20201207_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='shoeCategories',
        ),
        migrations.AlterField(
            model_name='shoe',
            name='shoeAvail',
            field=models.CharField(choices=[('In-stock', 'In Stock'), ('Sold-out', 'Sold Out'), ('Upcoming', 'Upcoming')], max_length=9),
        ),
    ]
