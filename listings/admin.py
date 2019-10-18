from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # afiseaza coloanele
    list_display_links = ('id', 'title')    # link pe aceste coloane, altfel doar pe prima
    list_filter = ('realtor',)              # filter
    list_editable = ('is_published',)       # camp editabil direct
    search_fields = ('title', 'description', 'address', 'city',  'state', 'zipcode', 'price')   # search
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
