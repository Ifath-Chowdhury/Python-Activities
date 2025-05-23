# 6.7 Project: Movie Recommender

# Prompt user to answer some questions
print("Anwer the following questions with yes or no\n")

pref1 = input("Do you like Action movies? ").lower()
pref2 = input("Do you like Comedy movies? ").lower()
pref3 = input("Do you like Romance movies? ").lower()

# Use logic operators to determine movie taste
if pref1:
    favGenre = "Action"
elif pref2:
    favGenre = "Comedy"
elif pref3:
    favGenre = "Romance"
elif pref1 and pref2 and not pref3:
    favGenre = "Action Comedy"
elif pref1 and not pref2 and pref3:
    favGenre = "Action Romance"
elif not pref1 and pref2 and pref3:
    favGenre = "Comedy Romance"
else:
    favGenre = "mid"

if favGenre == "Action Comedy":
    print("Watch Rush Hour")
elif favGenre == "Action Drama":
    print("Watch The Batman")
elif favGenre == "Comedy Drama":
    print("Watch The Intouchables")
elif favGenre == "Action":
    print("Watch The Raid")
elif favGenre == "Comedy":
    print("Watch Superbad")
elif favGenre == "Drama":
    print("Watch Forest Gump")
else:
    print("Your taste in movies sucks I'm not recommending anything to you")