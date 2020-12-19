# Generated by Django 3.1.4 on 2020-12-19 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0003_shoe_shoe_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='adminUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
