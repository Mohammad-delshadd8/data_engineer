from django.urls import path
from .views import deployment_sample

urlpatterns = [
    path('', deployment_sample, name='home'),
]

