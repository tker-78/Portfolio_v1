from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class DashboardView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'dashboard.html'

class GMOView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'gmo.html'

class OverviewView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'overview.html'

class DiaryView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary.html'
    context_object_name = 'diary_list'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

class StatusView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'status.html'


