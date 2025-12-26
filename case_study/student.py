
from typing import Dict, List

def add_student(db: Dict[str, dict], student_id: str, name: str, class_name: str) -> None:
    if student_id in db:
        raise ValueError(f"Student {student_id} already exists")
    db[student_id] = {"id": student_id, "name": name, "class": class_name,
                      "marks": {}, "attendance": [], "fees": []}

def get_student(db: Dict[str, dict], student_id: str) -> dict | None:
    return db.get(student_id)

def list_students(db: Dict[str, dict]) -> List[dict]:
    return list(db.values())
