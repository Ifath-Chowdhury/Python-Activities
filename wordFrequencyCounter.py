# 9.10 Project: Word Frequency Counter

text = "Sample text sentence. Some words are repeated and some are not maybe idk"

def CountWords(text):
    # Base case if text is empty
    if (text == ""):
        return {}
    
    # Convert to lowercase and remove punctuation
    text = text.lower().replace(".", "").replace(",", "").replace("?", "").replace("!", "")

    # Split text into words
    words = text.split()

    # Dictionary to store frequency of words
    frequencyOfWords = {}

    # Recursive helper function to recursively update dictionary untill all words are processed
    def UpdateDictionary(words, index):
        if index == len(words):
            return
        
        word = words[index]

        if word in frequencyOfWords:
            frequencyOfWords[word] += 1
        else:
            frequencyOfWords[word] = 1
        
        UpdateDictionary(words, index + 1)
    
    # Recursively call the function
    UpdateDictionary(words, 0)

    return frequencyOfWords

frequencyDictionary = CountWords(text)

for item, index in frequencyDictionary.items():
    print(f"{item}: {index}")