from django.urls import path

from . import views

app_name = 'HomeManager'
urlpatterns = [
    path('', views.index, name='index'),

    path('tache/<int:tache_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:tache_id>/updatedTask/', views.updatedTask, name='updatedTask'),

    path('<int:tache_id>/finishTask/', views.finishTask, name='finishTask'),

    path('createdTask/', views.createdTask, name='createdTask'),
]