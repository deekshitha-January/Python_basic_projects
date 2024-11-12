print("Welcome to my computer quiz")

playing = input("Do you want to play? ").strip().lower()

# Check if the user wants to play
if playing != "yes":
    quit()

print("Okay! Let's play : )")

score = 0

# Question 1
answer = input("What does CPU stand for? ").strip().lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Who is the Prime Minister of India? ").strip().lower()
if answer == "narendra modi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What is the national animal of India? ").strip().lower()
if answer == "bengal tiger":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Who is the Chief Minister of Andhra Pradesh? ").strip().lower()
if answer == "chandrababu naidu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your total score is:", score)
