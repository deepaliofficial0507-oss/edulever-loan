from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_loan, name="apply_loan"),
    path('confirm/', views.apply_confirm, name="apply_confirm"),
    path('submit/', views.apply_submit, name="apply_submit"),
    path('success/<int:loan_id>/', views.apply_success, name="apply_success"),
    path('status/', views.loan_status, name="loan_status"),
]
