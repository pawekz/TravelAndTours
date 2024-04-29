from django.contrib import admin

# Register your models here.
from .models import TourPackage, Review

admin.site.register(TourPackage)
admin.site.register(Review)

