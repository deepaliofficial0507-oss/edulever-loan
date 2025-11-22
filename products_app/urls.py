from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_home, name='products_home'),

    # Add these new routes for different product pages
    path('credit-card/', views.credit_card, name='credit_card'),
    path('home-loan/', views.home_loan, name='home_loan'),
    path('insurance/', views.insurance, name='insurance'),
]
