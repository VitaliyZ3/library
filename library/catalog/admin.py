from django.contrib import admin
from .models import Book,  Ticket
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']
    
admin.site.register(Book)
admin.site.register(Ticket)