from django.contrib import admin

class AquaParkList(admin.ModelAdmin):
    list_display = 

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)