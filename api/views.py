from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def ev_metrics(request):
    return Response([
        {
            "DEVICE_ID": "DEMO-001",
            "TIMESTAMP": "2024-01-01T08:00:00",
            "BATTERY_SOC": 85,
            "BATTERY_VOLTAGE": 400,
            "AMBIENT_TEMP": 22,
        }
    ])

@api_view(['GET'])
def ev_5min(request):
    return Response([
        {
            "DEVICE_ID": "DEMO-001",
            "WINDOW_START": "2024-01-01T08:00:00",
            "WINDOW_END": "2024-01-01T08:05:00",
        }
    ])

@api_view(['GET'])
def journeys(request):
    device_id = request.query_params.get('device_id')
    return Response([
        {
            "DEVICE_ID": device_id or "DEMO-001",
            "JOURNEY_START": "2024-01-01T08:00:00",
            "JOURNEY_END": "2024-01-01T09:00:00",
        }
    ])

@api_view(['GET'])
def journey_route(request):
    return Response([
        {
            "TS": "2024-01-01T08:00:00",
            "LATITUDE": -33.9249,
            "LONGITUDE": 18.4241,
            "SPEED": 60,
            "TOTAL_POWER": 120,
        }
    ])