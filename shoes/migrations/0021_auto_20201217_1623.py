# Generated by Django 3.1.4 on 2020-12-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0020_auto_20201217_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoeAvail', models.CharField(choices=[('In-stock', 'In Stock'), ('Sold-out', 'Sold Out'), ('Upcoming', 'Upcoming')], max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='shoe',
            name='shoeAvail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.availability'),
        ),
    ]
