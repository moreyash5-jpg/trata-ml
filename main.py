from fastapi import FastAPI

from scoring import calculate_all_metrics
from trend import calculate_weekly_trend
from alerts import generate_alerts, generate_recommendations


app = FastAPI(
    title="Trātā ML Engine",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "service": "Trātā ML Engine",
        "status": "running"
    }


@app.post("/calculate")
def calculate_metrics(data: dict):

    sleep_hours = float(data["sleep_hours"])
    daily_steps = int(data["daily_steps"])
    duty_hours = float(data["duty_hours"])

    metrics = calculate_all_metrics(
        sleep_hours,
        daily_steps,
        duty_hours
    )

    weekly_trend = calculate_weekly_trend(
        data.get("weekly_scores", [])
    )

    alerts = generate_alerts(
        metrics["workload_balance"],
        metrics["sleep_quality"],
        metrics["activity_index"]
    )

    recommendations = generate_recommendations(
        float(data.get("aqi", 0)),
        data.get("water_quality", "good")
    )

    return {
        "sleep": {
            "duration_hours": sleep_hours,
            "quality_percent": metrics["sleep_quality"]
        },

        "physical_activity": {
            "steps": daily_steps,
            "activity_percent": metrics["activity_index"]
        },

        "workload": {
            "duty_hours": duty_hours,
            "balance_percent": metrics["workload_balance"]
        },

        "overall_wellness": {
            "score_percent": metrics["overall_wellness"],
            "status": metrics["overall_status"]
        },

        "weekly_wellness_trend": weekly_trend,

        "alerts": alerts,

        "recommendations": recommendations
    }