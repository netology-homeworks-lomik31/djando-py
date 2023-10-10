from django.urls import path
from .views import SensorView, MeasurementView

urlpatterns = [
    path("sensors/", SensorView.as_view()),
    path("sensors/<int:id>/", SensorView.as_view()),
    path("measurements/", MeasurementView.as_view())
]
