from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'

class ShortcutsView(generic.TemplateView):
    template_name = 'shortcuts.html'

class OverviewView(generic.TemplateView):
    template_name = 'overview.html'

class EventsView(generic.TemplateView):
    template_name = 'events.html'

class ProfileView(generic.TemplateView):
    template_name = 'profile.html'

class StatusView(generic.TemplateView):
    template_name = 'status.html'
