from django.urls import path

from . import views

app_name = 'gmo'

urlpatterns = [
    path('', views.GmoIndexView.as_view(), name="gmo_index"),
    path('api/forex-status', views.ForexStatusAPI.as_view(), name="forex_status"),
    path('api/ticker', views.TickerAPI.as_view(), name="ticker"),
    path('api/klines/', views.KLinesAPI.as_view(), name="klines"),

]