from django.db import models
from django.utils import timezone

class Personne(models.Model):
    username_text = models.CharField(max_length=32, default=" ")
    prenom_text = models.CharField(max_length=32)
    nom_text = models.CharField(max_length=32)
    estActif_bool = models.BooleanField(default=True)
    metier_text = models.CharField(max_length=50, default= "Non renseigné")
    pourcentageAttribution_int = models.IntegerField(default=100)
    adresseMail_text = models.CharField(max_length=100, default=" ")
    creation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.prenom_text + " " + self.nom_text


class ParametrageTache(models.Model):
	libelleTache_text = models.CharField(max_length=120)
	tempsMoyenTraitementH_dec = models.FloatField(default=0)
	delaisJTolerance = models.IntegerField(default=1)
	def __str__(self):
		return self.libelleTache_text 


class Tache(models.Model):
    tache_text = models.CharField(max_length=120)
    creation_date = models.DateTimeField('Date de création')
    jalon_date = models.DateTimeField('Date Jalon de réalisation',default=timezone.datetime.max)
    commentaire_text = models.CharField(max_length=6000)
    priseEnChargePar_id = models.IntegerField(default=-1)
    creerPar_id =models.IntegerField(default=0)
    urgence_bool = models.BooleanField(default=False)
    codeTache_text = models.CharField(max_length=3)
    etat_text = models.CharField(max_length=2, default="EC")
    def __str__(self):
        if self.priseEnChargePar_id > 0:
            personne = Personne.objects.get(pk=self.priseEnChargePar_id)
            if personne:
                return f'{self.tache_text} (Pour : {personne.nom_text} {personne.prenom_text})'
        return self.tache_text

    def getCreerPar(self):
        if self.creerPar_id > 0:
            personne = Personne.objects.get(pk=self.creerPar_id)
            if personne:
                return f'{personne.nom_text} {personne.prenom_text}'
        return "Non renseigné"


class Crypto(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    code = models.CharField(max_length=3,primary_key = True)
    quantite = models.DecimalField(default=0, max_digits=10, decimal_places=9)
    def __str__(self):
        return self.code

    class Meta:
        ordering = ['code']

class TypoCrypto(models.Model):
    code = models.CharField(max_length=3)
    libelle = models.CharField(max_length=10)