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

@api_view(['GET'])
def manifest(request):
    return Response({
        "generated_at": "2026-01-01T00:00:00",
        "total_vehicles": 1,
        "vehicles": [
            {
                "fleet_number": "DEMO-001",
                "reg_number": "DEMO-REG",
                "make_model": "BYD B12",
                "vehicle_model": "B12",
                "vehicle_manufacturer": "BYD",
                "status": "Driving",
                "last_seen": "2026-01-01",
                "latest_timestamp": "2026-01-01T08:00:00",
                "latest_soc": 85.0,
                "latest_odometer_km": 10000.0,
                "latest_lat": -33.9249,
                "latest_lng": 18.4241,
                "latest_power_kw": 80.0,
                "latest_voltage": 600.0,
                "latest_current": 133.0,
                "gsm_signal": 80.0,
                "satellites": 10,
                "ext_voltage": 27.0,
                "int_battery": None,
                "distance_today_km": 50.0,
                "data_quality": "ok",
                "file": "DEMO-001.json"
            }
        ]
    })