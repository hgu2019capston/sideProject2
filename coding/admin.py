from django.contrib import admin
from .models import Coding


'''class CodingAdmin(admin.ModelAdmin):
    fieldsets = ['id', 'content']'''

admin.site.register(Coding)
