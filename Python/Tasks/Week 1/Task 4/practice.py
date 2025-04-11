# studentDetails = {
# #     "student1" : {
# #         "name":"Naman",
# #         "age":22,
# #         "Subject1": 98,
# #         "Subject2": 97
# #     },
# #     "student2" : {
# #         "name":"Harshit",
# #         "age":21,
# #         "Subject1": 90,
# #         "Subject2": 92
# #     },
# #     "student3" : {
# #         "name":"Sandy",
# #         "age":19,
# #         "Subject1": 88,
# #         "Subject2": 77
# #     },
# #     "student4" : {
# #         "name":"Nishant",
# #         "age":25,
# #         "Subject1": 48,
# #         "Subject2": 57
# #     }
# # }


# # print(studentDetails);

# # Initialize the dictionary to store student records
# students = {}

# def display_menu():
#     print("\nStudent Records Management")
#     print("1. View all student records")
#     print("2. Search for a student")
#     print("3. Add a new student")
#     print("4. Update marks of a student")
#     print("5. Exit")

# def view_records():
#     if students:
#         print("\nAll Student Records:")
#         for student, marks in students.items():
#             print(f"Name: {student}, Marks: {marks}")
#     else:
#         print("\nNo records found!")

# def search_student():
#     name = input("\nEnter the name of the student to search: ").strip()
#     if name in students:
#         print(f"Found: Name: {name}, Marks: {students[name]}")
#     else:
#         print("Student not found!")

# def add_student():
#     name = input("\nEnter the name of the new student: ").strip()
#     if name in students:
#         print("Student already exists!")
#     else:
#         try:
#             marks = float(input("Enter the marks of the student: "))
#             students[name] = marks
#             print("Student added successfully!")
#         except ValueError:
#             print("Invalid marks input. Try again.")

# def update_student():
#     name = input("\nEnter the name of the student to update: ").strip()
#     if name in students:
#         try:
#             marks = float(input("Enter the new marks: "))
#             students[name] = marks
#             print("Marks updated successfully!")
#         except ValueError:
#             print("Invalid marks input. Try again.")
#     else:
#         print("Student not found!")

# def main():
#     while True:
#         display_menu()
#         choice = input("\nEnter your choice (1-5): ").strip()
#         if choice == "1":
#             view_records()
#         elif choice == "2":
#             search_student()
#         elif choice == "3":
#             add_student()
#         elif choice == "4":
#             update_student()
#         elif choice == "5":
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# # Run the program
# main()