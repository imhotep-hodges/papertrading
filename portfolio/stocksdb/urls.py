from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addstock.html', views.addstock, name='addstock'),
    path('delete/<stock_id>', views.delete, name='delete'),

]