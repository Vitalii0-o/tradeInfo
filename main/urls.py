from django.urls import path
from main import views
urlpatterns = [
    path('', views.index),
    path('process_data', views.stock_sma, name="process_data"),
]
