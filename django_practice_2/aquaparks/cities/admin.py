from django.contrib import admin

class AquaParkList(admin.ModelAdmin):
    list_display = ("name", "address", "description", "cities")

    def cities(self, obj):
        return ", ".join([city.name for citi])

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)