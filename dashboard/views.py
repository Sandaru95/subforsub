from django.shortcuts import render, HttpResponse, redirect
from django.views import generic

from accounts.models import Signal_User_Profile
from .models import Comment

class IndexAccountView(generic.TemplateView):
    template_name = 'dashboard/index_account.html'
# ===================================================================================
# Find Others
class FindOtherPeopleView(generic.TemplateView):
    template_name = 'dashboard/find_other.html'

    def get_context_data(self, **kwargs):
        context = super(FindOtherPeopleView, self).get_context_data(**kwargs)
        context['users_list'] = Signal_User_Profile.objects.all().order_by('-id')[:11]
        return context
# Find Others : Detail
class FindOtherPeopleDetailView(generic.View):
    template_name = 'dashboard/find_other_detail.html'

    def get(self, request, pk):
        current_signal_profile = Signal_User_Profile.objects.get(pk=pk)
        context = {'object':current_signal_profile}
        context['owned_comment_list'] = Signal_User_Profile.objects.get(pk=pk).owned_comments.all()
        return render(request, self.template_name, context)

# Find Others : Detail : Comment
class FindOtherPeopleDetailCommentView(generic.View):
    def post(self, request, pk):
        commentValue = request.POST['comment-value']
        # Creating the new Comment
        new_comment = Comment()
        new_comment.owner_user_profile = request.user.signal_user_profile
        new_comment.comment_text = commentValue
        new_comment.save()
        # Adding this comment to the related Signal User
        current_viewed_signal_user = Signal_User_Profile.objects.get(id=pk)
        current_viewed_signal_user.owned_comments.add(new_comment)
        current_viewed_signal_user.save()

        # Returning Success Http Response
        return HttpResponse('Success!')

# =======================================================================================
# Find More Subscribers by Other Methods
class FindMoreSubscriberView(generic.View):
    template_name = 'dashboard/find_more_subscribers.html'

    def get(self, request):
        if (request.user.signal_user_profile.is_on_survey == True):
            return redirect('dashboard:subscribers_survey')
        else:
            return render(request, self.template_name, {})

# =======================================================================================
# Survey
class SubscribersSurveyView(generic.View):
    def get(self, request):
        # Setting That User is on a Survey
        request.user.signal_user_profile.is_on_survey = True
        request.user.signal_user_profile.save()
        # Getting all channels by survey points
        context = {}
        # Subtracting One from Survey points of rendering subscribers list
        channels_to_subscribe = []
        for channel in Signal_User_Profile.objects.all().order_by('survey_points')[:5]:
            channel.survey_points -= 1
            channel.save()
            channels_to_subscribe.append(channel)

        context['channels_to_subscribe'] =  channels_to_subscribe

        return render(request, 'dashboard/surveys/subscribers_survey.html', context)

    def post(self, request):
        print('We are on post!')
        request.user.signal_user_profile.survey_points += 5
        request.user.signal_user_profile.is_on_survey = False
        request.user.signal_user_profile.save()
        return HttpResponse('success')

# =======================================================================================
# Settings
class SettingsView(generic.TemplateView):
    template_name = 'dashboard/settings.html'
