# Generated by Django 3.1.4 on 2020-12-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0012_auto_20201208_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoeBrand',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
