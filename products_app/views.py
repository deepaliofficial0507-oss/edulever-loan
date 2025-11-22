from django.shortcuts import render

def products_home(request):
    return render(request, 'products_home.html')

def credit_card(request):
    return render(request, 'credit_card.html')

def home_loan(request):
    return render(request, 'home_loan.html')

def insurance(request):
    return render(request, 'insurance.html')
