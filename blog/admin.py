from django.contrib import admin
from . models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')
    # search_fields = ('title',)

class BlogContributorAdmin(admin.ModelAdmin):
    list_display = ('contribution', 'contributor')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('uploader', 'date_created')


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogContributors, BlogContributorAdmin)
admin.site.register(Photo, PhotoAdmin)
# Register your models here.
