
from typing import Dict
from datetime import datetime

class ReportGenerator:
    def __init__(self, db: Dict[str, dict]):
        self.db = db

    def generate_student_report(self, student_id: str) -> str:
        st = self.db.get(student_id)
        if not st:
            return f"Student {student_id} not found."
        lines = []
        lines.append(f"=== Report: {st['name']} ({st['id']}) ===")
        lines.append(f"Class: {st['class']}")
        if st["marks"]:
            lines.append("Marks:")
            for subj, score in st["marks"].items():
                lines.append(f"  - {subj}: {score}")
        else:
            lines.append("Marks: (no records)")
        present = sum(1 for a in st["attendance"] if a["present"])
        total = len(st["attendance"])
        pct = round((present / total * 100), 2) if total else 0
        lines.append(f"Attendance: {present}/{total} days ({pct}%)")
        total_paid = sum(p["amount"] for p in st["fees"])
        lines.append(f"Fees paid: ₹{total_paid:.2f}")
        lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        return "\n".join(lines)

    def generate_class_report(self) -> str:
        lines = ["=== Class Report ==="]
        for st in self.db.values():
            lines.append(f"{st['id']} - {st['name']} - Class {st['class']}")
        lines.append(f"Total students: {len(self.db)}")
        return "\n".join(lines)
