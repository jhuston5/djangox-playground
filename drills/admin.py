from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PDF, Drill
# Register your models here.

admin.site.register(Drill)
admin.site.register(PDF)