
from typing import Dict, List
from utils import validate_score

def record_marks(db: Dict[str, dict], student_id: str, subject: str, score: float) -> None:
    st = db.get(student_id)
    if not st:
        raise KeyError(f"Student {student_id} not found")
    validate_score(score)
    st["marks"][subject] = float(score)

def compute_average(db: Dict[str, dict], student_id: str) -> float:
    st = db.get(student_id)
    if not st or not st["marks"]:
        return 0.0
    scores: List[float] = list(st["marks"].values())
    return sum(scores) / len(scores)

def class_average(db: Dict[str, dict]) -> float:
    avgs: List[float] = []
    for st in db.values():
        if st["marks"]:
            scores = list(st["marks"].values())
            avgs.append(sum(scores) / len(scores))
    return (sum(avgs) / len(avgs)) if avgs else 0.0