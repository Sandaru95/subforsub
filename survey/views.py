from django.shortcuts import render, HttpResponse
from django.views import generic

from accounts.models import Signal_User_Profile

class FirstSurveyView(generic.TemplateView):
	template_name = 'survey/first_survey.html'

	def get(self, request):
		context = {}
		context['signal_profile_list'] = Signal_User_Profile.objects.all().order_by('-id')[1:6]
		return render(request, self.template_name, context)
	
	def post(self, request):
		request.user.signal_user_profile.has_survey_complete = True
		request.user.signal_user_profile.save()
		return HttpResponse('success')
