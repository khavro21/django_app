from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from blog.models import Article, Contact

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}  

class ContactAdmin(admin.ModelAdmin):
    readonly_fields=('name', 'email', 'date', )    

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact, ContactAdmin)
