from django.http import HttpResponse, HttpResponseRedirect
from .models import Tache, Personne
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.db.models import Q

def index(request):
	taches = Tache.objects.filter(Q(etat_text = 'EC') | Q(etat_text = 'EA'))\
	.order_by('-creation_date')
	context = {
		'taches' : taches,
	}
	return render(request, 'HomeManager/index.html', context)

def detail(request, tache_id):
	tache = None
	if tache_id > 0:
		tache = get_object_or_404(Tache, pk=tache_id)
	personnes = Personne.objects.filter(estActif_bool = True)
	return render(request, 'HomeManager/detail.html', {'tache': tache,
		'personnes': personnes})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def updatedTask(request, tache_id):
	tache = get_object_or_404(Tache, pk=tache_id)
	tache.commentaire_text = request.POST.get('commentaireTache', '')
	tache.priseEnChargePar_id = request.POST.get('selPriseEnCharge',0)
	tache.etat_text = request.POST.get('selEtat','EC')
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))

def createdTask(request):
	tache = Tache(
		tache_text = request.POST.get('titreTache','Aucun titre'),
		commentaire_text = request.POST.get('commentaireTache', ''),
		priseEnChargePar_id = request.POST.get('selPriseEnCharge',0),
		etat_text = 'EC',
		creation_date = timezone.now(),
		creerPar_id = 0)
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))

def finishTask(request, tache_id):
	tache = get_object_or_404(Tache, pk=tache_id)
	tache.etat_text = "RE"
	tache.save()
	return HttpResponseRedirect(reverse('HomeManager:index'))