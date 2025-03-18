from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class DashboardView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'dashboard.html'

class GMOView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'gmo.html'

class OverviewView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'overview.html'

class EventsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'events.html'

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

class StatusView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'status.html'

class InquiryView(generic.TemplateView):
    template_name = 'inquiry.html'