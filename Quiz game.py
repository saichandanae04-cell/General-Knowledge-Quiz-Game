# General Knowledge Quiz

score = 0

print("Welcome to the General Knowledge Quiz!")
print("-------------------------------------")


answer1 = input("1. What is the capital of France? ")

if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")


answer2 = input("2. Which planet is known as the Red Planet? ")

if answer2.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")


answer3 = input("3. How many days are there in a week? ")

if answer3 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final Score
print("\nQuiz Completed!")
print("Your Final Score:", score, "/ 3")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good Job!")
elif score == 1:
    print("Keep Practicing!")
else:
    print("Better luck next time!")