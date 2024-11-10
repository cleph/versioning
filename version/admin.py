from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Platform, Patch, Test, Bug

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'version', 'created_at', 'updated_at')
    search_fields = ('title', 'status')
    list_filter = ('status',)

@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform', 'created_at', 'updated_at')
    search_fields = ('title', 'platform__title')
    list_filter = ('platform',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform', 'created_at', 'updated_at')
    search_fields = ('title', 'platform__title')
    list_filter = ('platform',)

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform', 'created_at', 'updated_at')
    search_fields = ('title', 'platform__title')
    list_filter = ('platform',)
