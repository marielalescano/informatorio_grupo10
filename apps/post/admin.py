from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ObjetivoResource(resources.ModelResource):
    class Meta:
        model = Objetivo


class ObjetivoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = ObjetivoResource


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('titulo', 'estado', 'fecha_creacion',)
    resource_class = PostResource




admin.site.register(Post,PostAdmin)
admin.site.register(Objetivo,ObjetivoAdmin)


