from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = {'seller', 'title', 'description', 'image', 'start_price', 'condition', 'created_date'}

admin.site.register(Item)