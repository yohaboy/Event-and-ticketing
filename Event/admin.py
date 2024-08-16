from django.contrib import admin
from Event.models import EventModel,Location,Category
# Register your models here.

admin.site.register(EventModel)
admin.site.register(Location)
admin.site.register(Category)