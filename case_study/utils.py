
import random
import math
from datetime import date

def today_date() -> str:
    return date.today().isoformat()

def validate_score(score: float) -> None:
    if not (0 <= float(score) <= 100):
        raise ValueError("Score must be between 0 and 100")

def generate_random_ids(n: int, prefix: str = "S") -> list:
    ids = []
    for _ in range(n):
        num = random.randint(1000, 9999)
        ids.append(f"{prefix}{num}")
    return ids

def curve_score(score: float, curve_percent: float) -> int:
    curved = score * (1 + curve_percent / 100)
    return int(math.ceil(curved))
