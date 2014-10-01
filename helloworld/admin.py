from django.contrib import admin
from helloworld.models import MyUsers


class MyUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created', 'modified')
    search_fields = ('name', 'country')
    list_filter = ('created',)
    ordering = ('-name',)
    date_hierarchy = 'created'

admin.site.register(MyUsers, MyUsersAdmin)
