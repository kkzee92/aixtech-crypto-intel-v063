from crypto_intel.strategies.asset_class import score_signal

def test_score_signal_basic():
    factors = {"strength": 0.6, "vol_tier": 0.4, "anomaly": 0.2}
    score = score_signal("major", "trend", factors)
    assert 0 < score <= 0.08

def test_stress_returns_zero():
    factors = {"strength": 0.8}
    score = score_signal("major", "stress", factors)
    assert score == 0.0
