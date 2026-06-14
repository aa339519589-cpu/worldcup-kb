def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def match_result(score_a, score_b):
    if score_a > score_b:
        return 1.0
    if score_a < score_b:
        return 0.0
    return 0.5


def update_pair(rating_a, rating_b, score_a, score_b, k=32):
    expected_a = expected_score(rating_a, rating_b)
    result_a = match_result(score_a, score_b)
    new_a = rating_a + k * (result_a - expected_a)
    new_b = rating_b + k * ((1 - result_a) - (1 - expected_a))
    return new_a, new_b
