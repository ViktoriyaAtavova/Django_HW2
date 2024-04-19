# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import json
from rest_framework.response import Response
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement
from rest_framework import generics


class AllSensorView(generics.ListCreateAPIView):

  queryset = Sensor.objects.all()
  serializer_class = SensorDetailSerializer


class SensorView(generics.RetrieveUpdateAPIView):

  queryset = Sensor.objects.all()
  serializer_class = SensorDetailSerializer

  def post(self, request):
    json_data = json.loads(request.body)
    sensor = Sensor(name=json_data.get('name'), description=json_data.get('description'))
    sensor.save()
    return Response()

class MeasurementView(generics.CreateAPIView):

  queryset = Measurement.objects.all()
  serializer_class = MeasurementSerializer
  
  def post(self, request):
    json_data = json.loads(request.body)
    print(type(Sensor.objects))
    measurement = Measurement(
      sensor=Sensor.objects.get(pk=json_data.get('sensor')),
      temperature=json_data.get('temperature')
      )
    measurement.save()
    return Response()