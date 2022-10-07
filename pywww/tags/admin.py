from django.contrib import admin
from tags.models import Tag


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagAdmin)

# Register your models here.
from django.contrib import admin

# Register your models here.
