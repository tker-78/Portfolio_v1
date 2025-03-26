from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Diary
from .forms import DiaryCreateForm

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

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記を作成できませんでした。')
        return super().form_invalid(form)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

class StatusView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'status.html'


