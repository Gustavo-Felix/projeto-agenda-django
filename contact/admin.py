from django.contrib import admin # type:ignore
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...