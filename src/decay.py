def exponential_weight(year, current_year=2026, half_life=8):
    age = current_year - year
    if half_life <= 0:
        return 1
    return 0.5 ** (age / half_life)
