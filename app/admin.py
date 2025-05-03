from django.contrib import admin

from .models import *

class BbAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price')
    list_display_links = ('title',)
    search_fields = ('title', )

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
