from django.contrib import admin
from .models import Shoe, NewShoe, Brand, Sizes, Availability

# Register your models here.
admin.site.register(Shoe)
admin.site.register(NewShoe)
admin.site.register(Brand)
admin.site.register(Sizes)
admin.site.register(Availability)
