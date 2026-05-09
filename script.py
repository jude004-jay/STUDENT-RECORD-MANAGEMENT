student_record =()

def caculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "F"
    else:
        return "F"

def add_stduent():
    print("\n--- Add Student Record---")
    name=input("Enter student name: ")
    student_id = input("Enter student id: ")
    test_score = float(input("Enter Test Score: "))
    exam_score = float(input("Enter Exam Score: "))

    total = test_score + exam_score
    average = total / 2
    grade = caculate_grade(average)

    student = {
        "name": name,
        "student_id": student_id,
        "test_score": test_score,
        "exam_score": exam_score,
        "total": total,
        "average": average,
        "grade": grade
    }

    student.append(student_record)

def view_student():
    print("\n--- View Student Record---")
    if len(student_record) == 0:
        print("No Student Record")
    else:
        for student in student_record:
            print(".................")
            print(" name: ", student["name"])
            print(" student id: ", student["student_id"])
            print(" test scores: ", student["test_score"])
            print(" exam scores: ", student["exam_score"])
            print("total scores: ", student["total"])
            print("average scores: ", student["average"])
            print("grade: ", student["grade"])


while True:
    print("\n==== student_record====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_stduent()
    elif choice == 2:
        view_student()
    elif choice == 3:
        print("exiting program")
        break
    else:
        print("invalid choice")