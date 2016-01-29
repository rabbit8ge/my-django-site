print('debug: start blogs.admin')
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from models import Blogs, Categories
from django.contrib.admin.templatetags.admin_list import date_hierarchy
print('debug: finish import')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    fields = (('name',), ('slug',), )


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': CKEditorWidget } , }
    list_display = ['title', 'date', 'time', 'publish'] # list to display in table.
    fields = (('page_title',),('title', 'publish',), ('slug',), ('tags',), ('category',),('meta_description','meta_keywords',), 'body') # A sub-tuple in a line.
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('tags', 'publish', 'date')
    date_hierarchy = 'date' # Not tuple.
    search_fields = ['title', 'body'] # search field.
    #filter_horizontal = ('category',) # TODO: No take effect.
    #raw_id_fields = ('tags',) # TODO: Test.


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)
print('debug: finish blogs.admin')