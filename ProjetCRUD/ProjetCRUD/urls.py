from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.fruit_list, name='fruit_list'),
    path('fruit/<int:pk>/', views.fruit_detail, name='fruit_detail'),
    path('fruit/new/', views.fruit_create, name='fruit_create'),
    path('fruit/<int:pk>/edit/', views.fruit_update, name='fruit_update'),
    path('fruit/<int:pk>/delete/', views.fruit_delete, name='fruit_delete'),
]
