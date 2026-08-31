def generate_alerts(
    workload_balance: int,
    sleep_quality: int,
    activity_index: int
) -> dict:

    # Workload alert
    if workload_balance < 50:
        workload_alert = {
            "state": "Warning",
            "message": (
                f"Workload balance is currently at "
                f"{workload_balance}%. Consider monitoring "
                f"workload and rest periods."
            )
        }
    else:
        workload_alert = {
            "state": "Info",
            "message": (
                f"Workload balance is currently at "
                f"{workload_balance}%. "
                f"Continue monitoring workload and rest periods."
            )
        }

    # Sleep alert
    if sleep_quality >= 80:
        sleep_alert = {
            "state": "Success",
            "message": (
                f"Sleep quality is currently good at "
                f"{sleep_quality}%."
            )
        }
    else:
        sleep_alert = {
            "state": "Warning",
            "message": (
                f"Sleep quality is currently at "
                f"{sleep_quality}%. Consider prioritizing "
                f"adequate rest."
            )
        }

    # Activity alert
    if activity_index >= 60:
        activity_alert = {
            "state": "Success",
            "message": "Physical activity is within a healthy range."
        }
    else:
        activity_alert = {
            "state": "Warning",
            "message": "Physical activity is below the configured target range."
        }

    return {
        "workload_balance_alert": workload_alert,
        "sleep_quality_alert": sleep_alert,
        "physical_activity_alert": activity_alert
    }


def generate_recommendations(
    aqi: float,
    water_quality: str
) -> dict:

    # Air quality
    if aqi > 150:
        air_advisory = (
            "Consider reducing outdoor activity when "
            "air pollution levels are high."
        )
    else:
        air_advisory = (
            "Air quality is currently within the configured "
            "acceptable range."
        )

    # Water quality
    if water_quality.lower() in ["poor", "unsafe", "contaminated"]:
        water_advisory = (
            "Water quality requires attention. "
            "Follow preventive measures and monitor "
            "local water-quality updates."
        )
    else:
        water_advisory = (
            "Monitor water quality regularly and take "
            "preventive action when contamination levels increase."
        )

    # Environmental trigger
    if aqi > 200 or water_quality.lower() in ["unsafe", "contaminated"]:
        environmental_alert = (
            "Environmental conditions require immediate attention."
        )
    elif aqi > 100 or water_quality.lower() == "poor":
        environmental_alert = (
            "Environmental conditions require monitoring."
        )
    else:
        environmental_alert = (
            "Environmental conditions are within the configured range."
        )

    return {
        "water_quality_advisory": water_advisory,
        "air_quality_advisory": air_advisory,
        "environmental_alert": environmental_alert
    }