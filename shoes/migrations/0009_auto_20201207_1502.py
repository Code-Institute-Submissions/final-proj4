# Generated by Django 3.1.4 on 2020-12-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0008_auto_20201207_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='shoeCategories',
            field=models.CharField(choices=[('New-Release', 'NEW RELEASE'), ('Popular', 'POPULAR')], max_length=11),
        ),
    ]
