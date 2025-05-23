# 5.11 User Profile Generator

# Prompt user input
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

# String concat to make full name
fullName = firstName + " " + lastName

# String formatting for sentence with age, city and occupation
sentence = f"An {age} year old {occupation} living in {city}"

# Escape characters to include quotation marks and a new line in profile description
profileDescription = "\nTheir favourite quote is \"I LOVE YURI\""

# Modify full name and description with string methods
fullName = fullName.upper()
profileDescription = profileDescription.lower()

# Display full profile
print(f"\n{fullName}")
print(sentence)
print(profileDescription)