from django.contrib import admin

from .models import Personne, Tache, ParametrageTache

admin.site.register(Personne)
admin.site.register(Tache)
admin.site.register(ParametrageTache)