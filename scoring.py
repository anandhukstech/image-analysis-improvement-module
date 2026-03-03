def normalize(value, max_value):
    return min(max((value / max_value) * 100, 0), 100)

def calculate_quality_score(metrics):
    score = int((
        normalize(metrics["brightness"], 255) +
        normalize(metrics["contrast"], 80) +
        normalize(metrics["sharpness"], 1000)
    ) / 3)

    return score