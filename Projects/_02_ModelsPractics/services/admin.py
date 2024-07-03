from django.contrib import admin
from services.models import Services
# Register your models here.
class registerServices(admin.ModelAdmin):
    list_display = ("title","icon", "desc" )

admin.site.register(Services, registerServices)