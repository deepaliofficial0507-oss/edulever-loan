from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Home View
def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Accounts app handles Signup + Login
    path('accounts/', include('accounts.urls')),

    # Loans app handles Apply Loan + Loan Status
    path('loan/', include('loans.urls')),
    
    path("about/", TemplateView.as_view(template_name="about.html")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

