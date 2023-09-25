
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    marks1 = input("enter   marks1 : ")
    marks2 = input("enter   marks2 : ")
    marks3 = input("enter   marks3 : ")
    classs = input("enter the  classs : ")
    import os
   # os.mkdir("d:\\kiran")
    with open("d:\\kiran\\student.txt", "a+") as file:
     file.write(f" {student_id} , {name} , {grade} , {marks1}, {marks2},{marks3}, {classs} \n")
     print("Student record added successfully.")


while True:

    choice = input("Enter your choice (y/n): ")

    if choice == "y":
        (add_student())


    elif choice == "n":
        break
    else:
        print("Invalid choice. Please enter y, n")