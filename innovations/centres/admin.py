from django.contrib import admin

from .models import Center

admin.site.register(Center)
class CenterPostAdmin(admin.ModelAdmin):
    pass