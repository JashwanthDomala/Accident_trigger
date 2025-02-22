from django.urls import path
from .views import AccidentAlert

urlpatterns = [
    path('accident/', AccidentAlert.as_view(), name='accident_alert'),  # API to receive accident alerts
]
