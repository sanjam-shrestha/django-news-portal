from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','slug')
    list_display_links=('name',)
    prepopulated_fields={'slug': ('name',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category','get_image', 'date', 'page_views')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    ordering = ('-date', 'title')
    # fields = (('title', 'category'), 'description', 'image', ('slug', 'page_views'))
    readonly_fields = ('page_views',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
        else:
            return 'Image not found'

