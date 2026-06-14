from elo import expected_score


def predict_binary(rating_a, rating_b):
    p_a = expected_score(rating_a, rating_b)
    return {"team_a": p_a, "team_b": 1 - p_a}
