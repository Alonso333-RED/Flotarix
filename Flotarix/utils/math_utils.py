def normalize_dict(original_dict, max_value=1.0):
    total = sum(original_dict.values())
    if total == 0:
        return {k: 0 for k in original_dict}

    return {
        k: (v / total) * max_value
        for k, v in original_dict.items()
    }

def clamp(value, min_value=0.0, max_value=1.0):
    return max(min_value, min(value, max_value))