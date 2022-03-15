from django.urls import path
from .views import html_to_pdf, home

urlpatterns = [
    path('html-to-pdf/', html_to_pdf, name="html-to-pdf"),
    path('', home, name="home"),    
]