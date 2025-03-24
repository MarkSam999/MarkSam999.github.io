from django.contrib import admin
from .models import AquaPark, 

class CityList(admin.ModelAdmin):
    list_display = ("name", "description")

class AquaParkList(admin.ModelAdmin):
    list_display = ("name", "address", "description", "cities")

    def cities(self, obj):
        return ", ".join([city.name for city in obj.city.all()])
    
    cities.short_description = "City"

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)