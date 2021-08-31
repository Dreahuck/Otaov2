from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('HomeManager/', include('HomeManager.urls')),
    path('admin/', admin.site.urls),
]