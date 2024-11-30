quiz = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "What is the currency used in Japan?": "Yen",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the process by which plants make their food?": "Photosynthesis",
    "In which country is the Great Wall located?": "China",
    "What is the smallest prime number?": "2",
    "What organ pumps blood in the human body?": "Heart",
    "What is the square root of 64?": "8"
}
score = 0
for question,answer in quiz.items():
    print(question)
    user_input = input("what is your answer ? ")
    if user_input.strip().lower() == answer.lower():
        print("correct")
        score +=1
    else:
        print(f"Incorrect.The correct answer is {answer}.  ")
print(f"Your final score is {score} out of {len(quiz)}")
