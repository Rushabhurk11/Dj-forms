from django.contrib import admin
from .models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'email', 'address', 'phone')
    # search_fields = ('name', 'roll', 'email')
    # list_filter = ('roll',)
    # ordering = ('name',)
    # list_per_page = 10
admin.site.register(Student)