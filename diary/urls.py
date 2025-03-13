from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('shortcuts', views.ShortcutsView.as_view(), name='shortcuts'),
    path('overview', views.OverviewView.as_view(), name='overview'),
    path('events', views.EventsView.as_view(), name='events'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('status', views.StatusView.as_view(), name='status'),
]