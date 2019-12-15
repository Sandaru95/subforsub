from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dashboard.models import Comment

class Signal_User_Profile(models.Model):
    user_linked = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='signal_user_profile')
    name = models.CharField(max_length=500)
    channel_url = models.CharField(max_length=1000)
    created_on = models.DateTimeField(default=timezone.now)
    has_survey_complete = models.IntegerField(default=False)
    is_on_survey = models.BooleanField(default=False)
    survey_points = models.IntegerField(default=0)
    owned_comments = models.ManyToManyField(Comment) 
    
    def __str__(self):
        return self.name

