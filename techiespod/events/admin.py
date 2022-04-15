from django.contrib import admin
from .models import Venue, App
from . models import Event
from . models import MyClubUser
# Register your models here.

#admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(MyClubUser)
admin.site.register(App)

@admin.register(Venue)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'web')
    ordering = ('name',)
    search_fields = ('name', 'address', )