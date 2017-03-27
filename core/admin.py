from django.contrib import admin
from .models import Brand, Car, Fleet

# Register your models here.

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Fleet)