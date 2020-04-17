from django.contrib import admin
from .models import Area, GroupKnowledge


class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'slug']
    list_editable = ['rating', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Area, AreaAdmin)


class GroupKnowledgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'area_kn', 'rating', 'slug']
    list_filter = ['name', 'area_kn', 'rating', 'slug']
    list_editable = ['area_kn', 'rating']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(GroupKnowledge, GroupKnowledgeAdmin)

