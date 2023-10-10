from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer

class SensorView(APIView):
    def post(self, request):
        name = request.query_params.get("name")
        description = request.query_params.get("description")
        if (name is None or description is None): return Response({"status": "failed"})
        Sensor(
            name = name,
            description = description
        ).save()
        return Response({"status": "OK"})
    
    def patch(self, request, id):
        name = request.query_params.get("name")
        description = request.query_params.get("description")
        if (name is None or description is None): return Response({"status": "failed"})
        sensor = Sensor.objects.filter(id = id).first()
        sensor.name = name
        sensor.description = description
        sensor.save()
        return Response({"status": "OK"})
    
    def get(self, request, id = None):
        if id is None:
            ser_sensors = SensorSerializer(Sensor.objects.all(), many=True).data
        else:
            ser_sensors = SensorSerializer(Sensor.objects.filter(id=id).first()).data
            ser_measurements = MeasurementSerializer(Measurement.objects.filter(sensor=id).all(), many=True).data
            ser_sensors["measurements"] = ser_measurements
        return Response(ser_sensors)

class MeasurementView(APIView):
    def post(self, request):
        try:
            sensor = request.query_params.get("sensor")
            value = request.query_params.get("temperature")
        except: return Response({"status": "failed"})
        if (sensor is None or value is None): return Response({"status": "failed"})
        Measurement(
            sensor = Sensor.objects.filter(id = sensor).first(),
            value = value
        ).save()
        return Response({"status": "OK"})
