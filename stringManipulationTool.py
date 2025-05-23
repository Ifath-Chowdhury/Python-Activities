# 5.10 Project: String Manipulation Tool

# Prompt user input
userInput = input("Enter a string: ")

# Display menu of string manipulation options
stringManipOptions = "\nHere are your options for string manipulation:\n\n1. Convert to uppercase\n2. Convert to lowercase\n3. Slice string from a start index to an end index\n4. Calculate string length\n5. Loop through each character and display each on a new line\n"
print(stringManipOptions)

# Prompt user to enter their choice
choiceInput = input("Type the number corresponding to the option you want to pick: ")

def ManipulateString(userInput, choiceInput):
    if (choiceInput.isnumeric()):
        outputString = ""

        match choiceInput:
            case '1':
                outputString = userInput.upper()
            case '2':
                outputString = userInput.lower()
            case '3':
                startIndex = input("\nInput the starting index as a number: ")
                endIndex = input("\nInput the ending index as a number: ")
                if (startIndex.isnumeric() and endIndex.isnumeric()):
                    outputString = userInput[int(startIndex):int(endIndex)]
                else:
                    print("Invalid input")
            case '4':
                outputString = len(userInput)
            case '5':
                for letter in userInput:
                    print(f"\n{letter}")
        
        print(outputString)
    else:
        print("Invalid input. Try again.\n")
        print(stringManipOptions)
        choiceInput = input("Type the number corresponding to the option you want to pick: ")
        ManipulateString(userInput, choiceInput)

ManipulateString(userInput, choiceInput)


# Do the selected operation and display the result