# Generated by Django 3.1.4 on 2020-12-25 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='use_id',
            new_name='user_id',
        ),
    ]
