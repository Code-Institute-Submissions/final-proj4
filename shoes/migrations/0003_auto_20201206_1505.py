# Generated by Django 3.1.4 on 2020-12-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_shoe_soldout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]