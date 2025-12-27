def normalize_dict(to_normalize):
    total = sum(to_normalize.values())
    if total == 0:
        return {k: 0 for k in to_normalize}

    normalized = {
        k: int((v / total) * 100)
        for k, v in to_normalize.items()
    }

    difference = 100 - sum(normalized.values())
    if difference != 0:
        max_key = max(normalized, key=lambda k: normalized[k])
        normalized[max_key] += difference

    return normalized

def clamp(value, min_value=0.0, max_value=1.0):
    return max(min_value, min(value, max_value))