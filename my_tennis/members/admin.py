from django.contrib import admin
from . models import person
# Register your models here.

# admin.site.register(person)

class PersonAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "email","phone","joined_date")
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  
admin.site.register(person, PersonAdmin)