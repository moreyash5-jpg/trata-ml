def calculate_weekly_trend(daily_scores: list[int]) -> list[int]:
    """
    Returns the latest 7 wellness scores.
    """

    if len(daily_scores) >= 7:
        return daily_scores[-7:]

    if not daily_scores:
        return [0] * 7

    padding = [daily_scores[0]] * (7 - len(daily_scores))

    return padding + daily_scores


# Temporary test
if __name__ == "__main__":
    scores = [55, 65, 72, 60, 78, 70, 82]

    print(calculate_weekly_trend(scores))