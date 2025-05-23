# 8.7 Project: Student Record Management System

# Create tuples for student info
student1 = ("Hatsune Miku", 18, "Year 12")
student2 = ("Kasane Teto", 18, "Year 12")
student3 = ("Akita Neru", 18, "Year 12")

# Create a tuple of students
students = (student1, student2, student3)

# Count number of students
print(f"Number of students: {len(students)}")

# Find index of a specific student
print(f"Index of Teto: {students.index(student2)}")

# Create sets for student IDs and courses
studentIds = {1, 2, 3}
courses = {"Math", "English", "Science", "History"}
print(f"All courses: {courses}")

# Add student ids with update() method
newStudents = {4, 5}
studentIds.update(newStudents)

# Subtract completed courses from all courses to find remaining courses
completedCourses = {"Math", "English"}
remainingCourses = courses - completedCourses
print(f"Remaining Courses: {remainingCourses}")

# Use frozen sets
frozenCourses = frozenset(["Math", "English", "Science", "History"])
print(f"Frozen Courses: {frozenCourses}")

# Attempting to modify a frozen set will raise an AttributeError
# frozen_courses.add("Art")

# Create a frozen set of student data
frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")