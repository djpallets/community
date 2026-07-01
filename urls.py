from django.urls import path

from . import views

app_name = 'pallets'

urlpatterns = [
    # Base
    path('', views.dashboard, name='dashboard'),

    # Models
    path('models/<str:app_label>/<str:model_name>/', views.model_list, name='model_list'),
    path('models/<str:app_label>/<str:model_name>/new/', views.model_create, name='model_create'),
    path('models/<str:app_label>/<str:model_name>/<int:pk>/edit/', views.model_edit, name='model_edit'),
    path('models/<str:app_label>/<str:model_name>/<int:pk>/delete/', views.model_delete, name='model_delete'),
]
