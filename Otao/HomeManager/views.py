from django.http import HttpResponse, HttpResponseRedirect
from .models import Tache, Personne
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from datetime import datetime

def authorizedUser(request):
	if request.method == 'POST':
		password = request.POST['mdp']
		username = request.POST['username']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('HomeManager:index'))
		else:
			return render(request, 'HomeManager/connexion.html', {
            	'error_message_login': "Connexion refusé."
        	})


def index(request):
	taches = Tache.objects.filter(Q(etat_text = 'EC') | Q(etat_text = 'EA'))\
	.order_by('jalon_date', 'creation_date')
	listTaches = []
	for tache in taches:
		optTache = {
		'strTache' : str(tache),
		'titre' : tache.tache_text,
		'commentaire' : tache.commentaire_text,
		'creerPar_text' : tache.getCreerPar(),
		'id' : tache.id,
		'dateJalon' : tache.jalon_date
		}
		listTaches.append(optTache)
	context = {
		'taches' : listTaches,
	}
	return render(request, 'HomeManager/index.html', context)

def detail(request, tache_id):
	tache = None
	if tache_id > 0:
		tache = get_object_or_404(Tache, pk=tache_id)
	personnes = Personne.objects.filter(estActif_bool = True)
	return render(request, 'HomeManager/detail.html', {'tache': tache,
		'personnes': personnes})

def inscription(request):
	return render(request, 'HomeManager/inscription.html')

def connexion(request):
	return render(request, 'HomeManager/connexion.html')

def createdUser(request):
	if not request.POST['mdp'] == request.POST['confirmMdp']:
		return render(request, 'HomeManager/inscription.html', {
            'error_message_mdp': "Les mots de passe ne sont pas les mêmes."
        })
	if request.POST['mdp'] == "":
		return render(request, 'HomeManager/inscription.html', {
            'error_message_mdp': "Mot de passe manquant"
        })
	existing_user_by_mail = User.objects.filter(email=request.POST['email'])
	if existing_user_by_mail.count() > 0:
		return render(request, 'HomeManager/inscription.html', {
            'error_message_mailExist': "Cet email est déjà utilisé."
        })
	existing_user_by_username = User.objects.filter(username=request.POST['username'])
	if existing_user_by_username.count() > 0:
		return render(request, 'HomeManager/inscription.html', {
            'error_message_userExist': "Ce pseudo est déjà utilisé."
        })
	user = User.objects.create_user(request.POST['username'],
    	request.POST['email'], request.POST['mdp'], first_name=request.POST['nom'],
    	last_name=request.POST['prenom'])
	'''user.save()'''
	personne = Personne(username_text=request.POST['username'],
    	adresseMail_text=request.POST['email'],
    	prenom_text=request.POST['prenom'],
    	nom_text=request.POST['nom']
    	)
	personne.save()
	user = authenticate(username=request.POST['username'], password=request.POST['mdp'])
	if user:
		if user.is_active:
			auth_login(request, user)
			return HttpResponseRedirect(reverse('HomeManager:index'))
	HttpResponseRedirect(reverse('HomeManager:index'))

def updatedTask(request, tache_id):
	tache = get_object_or_404(Tache, pk=tache_id)
	dateJalon = request.POST.get('dateJalon', None)
	if dateJalon:
		tache.jalon_date = datetime.strptime(dateJalon,'%Y-%m-%d')
	tache.commentaire_text = request.POST.get('commentaireTache', '')
	tache.priseEnChargePar_id = request.POST.get('selPriseEnCharge',0)
	tache.etat_text = request.POST.get('selEtat','EC')
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))

def createdTask(request):
	userConnected = Personne.objects.get(username_text=request.user.username)
	tache = Tache(
		tache_text = request.POST.get('titreTache','Aucun titre'),
		commentaire_text = request.POST.get('commentaireTache', ''),
		priseEnChargePar_id = request.POST.get('selPriseEnCharge',0),
		etat_text = 'EC',
		creation_date = timezone.now(),
		creerPar_id = userConnected.id,
	)
	dateJalon = request.POST.get('dateJalon', None)
	if dateJalon:
		tache.jalon_date = datetime.strptime(dateJalon,'%Y-%m-%d')
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))

def finishTask(request, tache_id):
	tache = get_object_or_404(Tache, pk=tache_id)
	tache.etat_text = "RE"
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))