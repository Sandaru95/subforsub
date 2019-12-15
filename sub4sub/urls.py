from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.returnToHome),

    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('survey/', include('survey.urls')),
    path('dashboard/', include('dashboard.urls')),
]
