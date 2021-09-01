from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'HomeManager'
urlpatterns = [
    path('', views.index, name='index'),

    path("logout/", LogoutView.as_view(), name="logout"),

    path('tache/<int:tache_id>/', views.detail, name='detail'),

    path('<int:tache_id>/updatedTask/', views.updatedTask, name='updatedTask'),

    path('<int:tache_id>/finishTask/', views.finishTask, name='finishTask'),

    path('createdTask/', views.createdTask, name='createdTask'),

    path('inscription/', views.inscription, name='inscription'),

    path('connexion/', views.connexion, name='connexion'),

    path('createdUser/', views.createdUser, name='createdUser'),

    path('authorizedUser/', views.authorizedUser, name='authorizedUser'),
]