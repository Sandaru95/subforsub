from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
	path('first/', views.FirstSurveyView.as_view(), name='first_survey'),
]