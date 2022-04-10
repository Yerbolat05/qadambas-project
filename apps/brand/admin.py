from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from brand.models import Account, Clothes

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = (
        'description'
    )
    readonly_fields = ()

class ClothesAdmin(admin.ModelAdmin):
    readonly_fields = (
        
    )
    readonly_fields = ()



admin.site.register(Account,AccountAdmin)
admin.site.register(Clothes,ClothesAdmin)