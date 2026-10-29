students_total = 0
def read_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"Value must be no greater than {maximum}.")
        else:
            return value


def get_grade(average):
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


while True:
    print("=========================================================")
    print("STUDENT REPORT CARD")
    print("=========================================================")
    number_of_students = read_integer("Enter the number of students: ", minimum=1)
    number_of_subjects = read_integer("Enter the number of subjects: ", minimum=1)
    reports = []

    for student_number in range(1, number_of_students + 1):
        print(f"\n---- Student {student_number} ----")
        name = input("Enter student name: ").strip() or f"Student {student_number}"
        total_marks = 0

        for subject_number in range(1, number_of_subjects + 1):
            subject_name = input(f"Enter name of subject {subject_number}: ").strip()
            subject_name = subject_name or f"Subject {subject_number}"
            total_marks += read_integer(
                f"Enter marks out of 100 for {subject_name}: ", minimum=0, maximum=100
            )

        average = total_marks / number_of_subjects
        grade = get_grade(average)
        reports.append({"name": name, "total": total_marks, "average": average, "grade": grade})
        print(f"Student name: {name}")
        print(f"Total marks: {total_marks}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")

    class_average = sum(report["average"] for report in reports) / number_of_students
    passed_students = sum(report["average"] >= 50 for report in reports)
    pass_rate = passed_students / number_of_students * 100
    top_student = max(reports, key=lambda report: report["average"])
    lowest_student = min(reports, key=lambda report: report["average"])

    print("==============================================")
    print("CLASS SUMMARY")
    print(f"Class average: {class_average:.2f}")
    print(f"Number of students passed: {passed_students}")
    print(f"Pass rate: {pass_rate:.2f}%")
    print(f"Top student: {top_student['name']} ({top_student['average']:.2f})")
    print(f"lowest student: {lowest_student['name']} ({lowest_student['average']:.2f})")
    

    choice = input("\nDo you want to enter another class? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("Exiting the grading system. Goodbye!")
        break