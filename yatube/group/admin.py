from django.contrib import admin
from .models import Group


# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "tittle", "description", "slug")
    search_fields = ("tittle", "description")
    empty_value_display = "-пусто-"


admin.site.register(Group, GroupAdmin)
