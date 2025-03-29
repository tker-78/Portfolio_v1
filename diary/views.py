import os
import markdown
import random



from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
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
    paginate_by = 5
    ordering = ['-created_at']

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

    def get_context_data(self, **kwargs):
        """
        markdownでレンダリングする
        """
        context = super().get_context_data(**kwargs)
        context['rendered_as_markdown'] = markdown.markdown(self.object.content)
        return context

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    """
    日記の新規作成
    """

    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        success_url = reverse_lazy('diary:diary_detail', kwargs={'pk': self.object.pk })
        return success_url

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user

        images_dir = os.path.join('static', 'assets', 'images', 'diary_header')

        image_files = [f for f in os.listdir(images_dir)
                       if f.lower().endswith(('.jpg', '.png'))
                       ]

        if image_files:
            random_image_path = random.choice(image_files)
            diary.image_path = os.path.join('assets', 'images', 'diary_header', random_image_path)



        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記を作成できませんでした。')
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.warning(self.request, '日記を削除しました。')
        return super().form_valid(form)




class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

class StatusView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'status.html'


