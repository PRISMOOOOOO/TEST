from django.urls import path
from .views import display_text

urlpatterns = [
    path('display/', display_text, name='display_text'),
]
