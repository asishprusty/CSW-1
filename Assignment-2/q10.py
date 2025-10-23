def process_students(profiles):
    skill_counts = {}  # To count total occurrences of each skill
    top_student = None
    highest_avg = -1
    
    print("Average Marks per Student:")
    for student in profiles:
        # Extract info
        student_id, name = student["info"]
        
        # Calculate average marks
        marks = student["marks"]
        avg_marks = sum(marks) / len(marks) if marks else 0
        print(f"{name} (ID: {student_id}) - Average Marks: {avg_marks:.2f}")
        
        # Update top performer
        if avg_marks > highest_avg:
            highest_avg = avg_marks
            top_student = name
        
        # Count skills
        for skill in student["skills"]:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
    
    print("\nOverall Skill Frequency:")
    for skill, count in skill_counts.items():
        print(f"{skill}: {count}")
    
    print(f"\nTop-performing student: {top_student} with average marks {highest_avg:.2f}")

# Example usage:
students = [
    {
        "info": (101, "Alice"),
        "marks": [85, 90, 78],
        "skills": {"Python", "Java", "C++"}
    },
    {
        "info": (102, "Bob"),
        "marks": [92, 88, 95],
        "skills": {"Java", "C#", "Python"}
    },
    {
        "info": (103, "Charlie"),
        "marks": [70, 75, 80],
        "skills": {"C", "C++"}
    }
]

process_students(students)
