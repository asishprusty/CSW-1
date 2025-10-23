# Function to find the student with the highest average score
def top_student(student_scores):
    highest_avg = 0
    top_name = ""

    for name, scores in student_scores.items():
        if len(scores) == 0:
            continue  # skip if no scores
        avg = sum(scores) / len(scores)
        print(f"{name}'s Average: {avg:.2f}")  # optional: show all averages

        if avg > highest_avg:
            highest_avg = avg
            top_name = name

    return top_name


# ----- MAIN PROGRAM -----
students_scores = {
    "Ram": [85, 90, 92],
    "Laxman": [70, 80, 88],
    "Janaki": [95, 100, 90]
}

# Find top student
topper = top_student(students_scores)
print(f"\nTop Student: {topper}")
