from django.urls import path

from measurement.views import AllSensorView, MeasurementView, SensorView

urlpatterns = [
    path('sensors/', AllSensorView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
