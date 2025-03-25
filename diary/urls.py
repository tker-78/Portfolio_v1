from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('gmo', views.GMOView.as_view(), name='gmo'),
    path('overview', views.OverviewView.as_view(), name='overview'),
    path('diary', views.DiaryView.as_view(), name='diary'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('status', views.StatusView.as_view(), name='status'),
]