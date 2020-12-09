from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField


# Create your models here.
class Shoe(models.Model):
    SHOE_AVAILABILITY = (
        ('In-stock', 'In Stock'),
        ('Sold-out', 'Sold Out'),
        ('Upcoming', 'Upcoming')
    )

    SHOE_SIZES = (
        ('5', '5'),
        ('5.5', '5.5'),
        ('6', '6'),
        ('6.5', '6.5'),
        ('7', '7'),
        ('7.5', '7.5'),
        ('8', '8'),
        ('8.5', '8.5'),
        ('9', '9'),
        ('9.5', '9.5'),
        ('10', '10'),
        ('10.5', '10.5'),
        ('11', '11'),
    )

    shoeModel = models.CharField(blank=False, max_length=255)
    shoeBrand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    size = MultiSelectField(choices=SHOE_SIZES)
    shoeAvail = models.CharField(max_length=9, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.shoeModel + "" + self.shoeBrand


class NewShoe(models.Model):
    SHOE_AVAILABILITY = (
        ('In-stock', 'In Stock'),
        ('Sold-out', 'Sold Out'),
        ('Coming-Soon', 'Coming Soon')
    )

    shoeModel = models.CharField(blank=False, max_length=255)
    shoeBrand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    releaseDate = models.DateTimeField(default=datetime.now, blank=True)
    shoeAvail = models.CharField(max_length=11, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.shoeModel