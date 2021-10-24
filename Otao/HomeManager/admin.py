from django.contrib import admin

from .models import Crypto, Personne, Tache, ParametrageTache, TypoCrypto

admin.site.register(Personne)
admin.site.register(Tache)
admin.site.register(ParametrageTache)
admin.site.register(TypoCrypto)
admin.site.register(Crypto)