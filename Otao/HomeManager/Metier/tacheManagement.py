from HomeManager.models import Personne
from django.shortcuts import get_object_or_404
from django.utils import timezone


def changer_etat_tache(tache, etat_tache,user_id):
    tache.etat_text = etat_tache
    tache.save()
    if (tache.tchouCoin > 0):
        user = get_object_or_404(Personne,username_text=user_id)
        if tache.jalon_date >= timezone.now():
            user.tchouCoinWallet += tache.tchouCoin
        else :
            user.tchouCoinWallet += (tache.tchouCoin/2)
        user.save()
