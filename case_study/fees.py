
from typing import Dict
from utils import today_date

def record_fee(db: Dict[str, dict], student_id: str, amount: float, dt=None) -> None:
    st = db.get(student_id)
    if not st:
        raise KeyError(f"Student {student_id} not found")
    if dt is None:
        dt = today_date()
    st["fees"].append({"date": dt, "amount": float(amount)})

def total_paid(db: Dict[str, dict], student_id: str) -> float:
    st = db.get(student_id)
    if not st:
        return 0.0
    return sum(p["amount"] for p in st["fees"])

def pending_fee(db: Dict[str, dict], student_id: str, total_due: float) -> float:
    paid = total_paid(db, student_id)
    return round(float(total_due) - paid, 2)
