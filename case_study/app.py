
import student                              # import module
from marks import record_marks, compute_average  # from ... import
import report as rpt                        # module alias
from utils import today_date as today, generate_random_ids
import attendance, fees

import math
from datetime import timedelta, datetime
import random

from meta_demo import show_properties

def seed_data(db: dict) -> None:
    student.add_student(db, 'S1001', 'Aarav Sharma', '10-A')
    student.add_student(db, 'S1002', 'Diya Patel', '10-A')

    record_marks(db, 'S1001', 'Maths', 78)
    record_marks(db, 'S1001', 'Science', 85)
    record_marks(db, 'S1002', 'Maths', 92)

    attendance.mark_attendance(db, 'S1001', present=True)
    attendance.mark_attendance(db, 'S1001', present=False)
    attendance.mark_attendance(db, 'S1002', present=True)

    fees.record_fee(db, 'S1001', 5000.0)
    fees.record_fee(db, 'S1002', 5000.0)

def demonstrate_builtins() -> None:
    print('\n--- Built-in modules demo ---')
    s = 79.2
    curved = math.ceil(s * 1.05)
    print(f'Curved score using math.ceil: {curved}')
    dt = datetime.today() + timedelta(days=7)
    print(f"Next test date (datetime + timedelta): {dt.strftime('%Y-%m-%d')}")
    subject = random.choice(['Maths', 'Science', 'English'])
    print(f'Randomly selected subject: {subject}')

def main() -> None:
    db: dict = {}
    seed_data(db)

    print(f"Today's date from utils.today(): {today()}")
    print(f'Generated random IDs: {generate_random_ids(3)}')

    avg1 = compute_average(db, 'S1001')
    print(f'S1001 average: {avg1:.2f}')

    class_avg = math.floor(sum(compute_average(db, sid) for sid in db.keys()) / len(db))
    print(f'Class average (floored): {class_avg}')

    summary = attendance.attendance_summary(db, 'S1001')
    print(f'S1001 attendance: {summary}')

    pending = fees.pending_fee(db, 'S1001', total_due=10000)
    print(f'Pending fee for S1001: ₹{pending:.2f}')

    rg = rpt.ReportGenerator(db)
    print('\n' + rg.generate_student_report('S1001'))
    print('\n' + rg.generate_class_report())

    print('\n--- Module properties ---')
    show_properties(student)  # user-defined module
    show_properties(rpt)      # alias module
    import sys
    show_properties(sys)      # standard library module

    demonstrate_builtins()

if __name__ == '__main__':
    main()
