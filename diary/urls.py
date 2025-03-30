from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('gmo', views.GMOView.as_view(), name='gmo'),
    path('overview', views.OverviewView.as_view(), name='overview'),
    path('diary', views.DiaryView.as_view(), name='diary'),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary-create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),

    path('profile', views.ProfileView.as_view(), name='profile'),
    path('status', views.StatusView.as_view(), name='status'),
    path('api/calendar-data', views.CalendarDataAPIView.as_view(), name='calendar-data-api'),
]