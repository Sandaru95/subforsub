from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.IndexAccountView.as_view(), name='index_account'),
    path('findOther/', views.FindOtherPeopleView.as_view(), name='find_other'),
    path('findOther/detail/<int:pk>/', views.FindOtherPeopleDetailView.as_view(), name='find_other_detail'),
    path('findOther/detail/<int:pk>/comment/', views.FindOtherPeopleDetailCommentView.as_view(), name='find_other_detail_comment'),

    path('findMoreSubscribers/', views.FindMoreSubscriberView.as_view(), name='find_more_subscribers'),
    
    path('subscribersSurvey/', views.SubscribersSurveyView.as_view(), name='subscribers_survey'),

    path('settings/', views.SettingsView.as_view(), name='settings'),
]