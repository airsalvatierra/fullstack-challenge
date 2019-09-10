from django.contrib import admin

# Register your models here.
from apps.base.models import Categories, Books

class CategoriesAdmin(admin.ModelAdmin):
    fields = ['id','name']
    list_display = ['id','name',]

class BooksAdmin(admin.ModelAdmin):
    fields = ['category_id','title']
    list_display = ['category_id','title']


# Register your models here.
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Books,BooksAdmin)
