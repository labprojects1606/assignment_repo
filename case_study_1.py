# Student Grade Calculator using Dictionary

# Dictionary: student name -> list of marks
students = {
    "Ravi": [92, 88, 79],
    "Asha": [76, 81, 85],
    "Kabir": [64, 72, 69],
    "Meera": [55, 58, 61],
    "Pooja": [95, 93, 97]
}


# Function to calculate average
def calculate_average(marks):
    return sum(marks)/ len(marks)

# Function to assign grade
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


# Track top scorer
top_name = ""
top_avg = 0

print("Name\tAverage\tGrade")
for name, marks in students.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    print(f"{name}\t{avg:.2f}\t{grade}")

    # Check top scorer
    if avg > top_avg:
        top_avg = avg
        top_name = name

# Display top scorer
print("\nTop Scorer:")
print(f"{top_name} with average {top_avg:.2f}")
