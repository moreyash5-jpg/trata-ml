def calculate_sleep_quality(sleep_hours: float) -> int:
    """
    Prototype sleep quality index.
    Target reference: 8 hours.
    """
    score = (sleep_hours / 8.0) * 100
    return round(max(0, min(score, 100)))


def calculate_activity_index(daily_steps: int) -> int:
    """
    Prototype physical activity index.
    Target reference: 8,000 steps/day.
    """
    score = (daily_steps / 8000.0) * 100
    return round(max(0, min(score, 100)))


def calculate_workload_balance(duty_hours: float) -> int:
    """
    Prototype workload balance index.
    8 duty hours is treated as the balance reference.
    """
    excess_hours = max(0, duty_hours - 8)

    score = 100 - (excess_hours * 12.5)

    return round(max(0, min(score, 100)))


def calculate_overall_wellness(
    sleep_quality: int,
    activity_index: int,
    workload_balance: int
) -> int:
    """
    Weighted composite wellness score.
    """

    score = (
        sleep_quality * 0.40
        + activity_index * 0.30
        + workload_balance * 0.30
    )

    return round(max(0, min(score, 100)))


def get_wellness_status(score: int) -> str:

    if score >= 80:
        return "Good"

    if score >= 50:
        return "Moderate"

    return "Critical"


def calculate_all_metrics(
    sleep_hours: float,
    daily_steps: int,
    duty_hours: float
) -> dict:

    sleep_quality = calculate_sleep_quality(sleep_hours)

    activity_index = calculate_activity_index(daily_steps)

    workload_balance = calculate_workload_balance(duty_hours)

    overall_wellness = calculate_overall_wellness(
        sleep_quality,
        activity_index,
        workload_balance
    )

    return {
        "sleep_quality": sleep_quality,
        "activity_index": activity_index,
        "workload_balance": workload_balance,
        "overall_wellness": overall_wellness,
        "overall_status": get_wellness_status(overall_wellness)
    }


# Temporary test
if __name__ == "__main__":

    result = calculate_all_metrics(
        sleep_hours=7.4,
        daily_steps=6420,
        duty_hours=8
    )

    print(result)