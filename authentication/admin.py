from django.contrib import admin
from . models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name')
    # search_fields = ('username')

admin.site.register(User, UserAdmin)

# Register your models here.
