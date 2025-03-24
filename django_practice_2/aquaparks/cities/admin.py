from django.contrib import admin

class AquaParkList(admin.ModelAdmin):
    list_display = ("name", "address", "description", "cities")

    def cities

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)