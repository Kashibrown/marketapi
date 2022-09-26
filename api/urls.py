from django.urls import path 
from .views import * 

urlpatterns = [
    path('', api_overview, name= 'api-overview'),
    path('market-list/', marketList, name='market-list'),
    path('market-detail/<str:pk>/', marketDetail, name='market-detail'),
    path('market-create/', marketCreate, name='market-create'),
    path('market-update/<str:pk>/', marketUpdate, name='market-update'),
    path('market-delete/<str:pk>/', marketDelete, name='market-delete'),
    
]
