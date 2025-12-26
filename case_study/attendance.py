
from typing import Dict
from utils import today_date
from datetime import date as date_cls

def mark_attendance(db: Dict[str, dict], student_id: str, dt=None, present: bool = True) -> None:
    st = db.get(student_id)
    if not st:
        raise KeyError(f"Student {student_id} not found")
    if dt is None:
        dt = today_date()
    elif isinstance(dt, date_cls):
        dt = dt.isoformat()
    st["attendance"].append({"date": dt, "present": bool(present)})

def attendance_summary(db: Dict[str, dict], student_id: str) -> dict:
    st = db.get(student_id)
    if not st:
        return {"present": 0, "total": 0, "percentage": 0}
    total = len(st["attendance"])
    present = sum(1 for a in st["attendance"] if a["present"])
    pct = (present / total * 100) if total else 0
    return {"present": present, "total": total, "percentage": round(pct, 2)}
