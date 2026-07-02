from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
SAMPLE = {
    "Start_Time": "2026-01-15T08:30:00",
    "End_Time": "2026-01-15T09:30:00",
    "Distance(mi)": 1.2,
    "Temperature(F)": 45.0,
    "Wind_Chill(F)": 40.0,
    "Humidity(%)": 80.0,
    "Pressure(in)": 29.8,
    "Visibility(mi)": 6.0,
    "Wind_Speed(mph)": 12.0,
    "Precipitation(in)": 0.0,
    "Weather_Condition": "Cloudy",
    "Wind_Direction": "W",
    "State": "CA",
    "Sunrise_Sunset": "Day",
    "Civil_Twilight": "Day",
    "Junction": True,
    "Traffic_Signal": True,
}


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_severity():
    r = client.post("/predict/severity", json=SAMPLE)
    assert r.status_code == 200
    body = r.json()
    assert body["predicted_class"] in ("High Severity", "Low Severity")
    assert 0.0 <= body["high_severity_probability"] <= 1.0


def test_predict_duration():
    sample = {**SAMPLE}
    del sample["End_Time"]  
    r = client.post("/predict/duration", json=sample)
    assert r.status_code == 200
    assert r.json()["predicted_duration_minutes"] > 0
