

# Register your models here.
from django.contrib import admin
from .models import Destination, TravelPlan

admin.site.register(Destination)
admin.site.register(TravelPlan)