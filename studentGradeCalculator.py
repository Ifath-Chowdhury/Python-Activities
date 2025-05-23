# 7.11 Project: Student Grade Calculator

# List of student scores
scores = [51, 85, 90, 21 , 50, 46, 70, 80, 64 , 75]

# Calculate average with floor division
total = sum(scores)
numberOfScores = len(scores)
average = total // numberOfScores

# Comparison operators to determine grade
if average > 90:
    grade = "A"
if average > 80:
    grade = "B"
if average > 70:
    grade = "C"
if average > 60:
    grade = "D"
else:
    grade = "F"

# Update the grade using assignment operators
if average % 10 >= 5:
    grade += "+"

# Membership operators to check if a score exists in the list
checkScore = 58
if checkScore in scores:
    print(f"The score {checkScore} exists in the list")
else:
    print(f"The score {checkScore} does not exist in the list")

# Identity operators to compare objects
scores_copy = scores
if scores is scores_copy:
    print("scores and scores_copy are the same")
else:
    print("scores and scores_copy are different")

# Perform bitwise operations on the scores
bitwiseResult = scores[0] & scores[1]
print(f"Bitwise AND operation on the first two scores in the list: {bitwiseResult}")

# Display the student's grade
print(f"The student achieved an average score of {average} and their grade is {grade}")