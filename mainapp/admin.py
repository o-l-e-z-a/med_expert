from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import License, Company, Category, Service, News, CompanyType


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'date')
    list_display_links = ('name', 'url', 'description', 'date')
    list_filter = ('date', )
    save_as = True
    save_on_top = True
    prepopulated_fields = {"url": ("name",)}


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')
    list_display_links = ('name', 'photo')
    save_as = True
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id', 'description', 'url')
    list_display_links = ('name', 'parent_id', 'description', 'url')
    list_filter = ('parent_id', )
    save_as = True
    save_on_top = True
    prepopulated_fields = {"url": ("name",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_display_links = ('name', 'price', 'category')
    list_filter = ('category', )
    save_as = True
    save_on_top = True


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    save_as = True
    prepopulated_fields = {"url": ("name",)}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_display_links = ('name', 'type')
    list_filter = ('type', )
    save_as = True

