from django.urls import path

from . import views

app_name = 'gmo'

urlpatterns = [
    path('', views.GmoIndexView.as_view(), name="gmo_index"),
    path('api/forex-status', views.ForexStatus.as_view(), name="forex_status"),

]