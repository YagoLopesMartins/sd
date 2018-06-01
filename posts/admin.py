from django.contrib import admin

from .models import Posts

# Register your models here.

"""
    Esta linha habilita o uso interno do admin do django,
    facilitando o trabalho de CRUD da aplicação
"""
admin.site.register(Posts)
