from django.contrib import admin

class CityList(admin.ModelAdmin):
    

class AquaParkList(admin.ModelAdmin):
    list_display = ("name", "address", "description", "cities")

    def cities(self, obj):
        return ", ".join([city.name for city in obj.city.all()])
    
    cities.short_description = "City"

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)