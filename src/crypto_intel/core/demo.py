"""Paper-only demo runner. Research only."""
from crypto_intel.strategies.asset_class import score_signal

def run_demo():
    print("AIxTech crypto intel v0.63 paper-only demo")
    print("No live execution. Synthetic factors only.")
    factors = {"strength": 0.6, "vol_tier": 0.4, "anomaly": 0.2, "correlation": 0.3, "vol_forecast": 0.45}
    score = score_signal("major", "trend", factors)
    print(f"Sample major score: {score}")
    print("See docs/ for full playbooks and security architecture.")
