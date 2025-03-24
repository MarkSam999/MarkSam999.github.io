from django.contrib import admin

class AquaParkList(admin.ModelAdmin):
    

admin.site.register(AquaPark, AquaParkList)
admin.site.register(City, CityList)