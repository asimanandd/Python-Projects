Questions = ["What is the capital of Djibouti?",
             "Which of the following country is located in South America?",
             "Which country shares a coastal boundary with Indian ocean?",
             "Which one is the neighbouring country with France?",
             "In which country, 'Thames' river is located?"]

Options = [["A. New Jersey", "B. Djibouti", "C. Sudan", "D. Cape Town"],
           ["A. Mexico", "B. Canada", "C. Peru", "D. Brunei"],
           ["A. Spain", "B. USA", "C. Singapore", "D. Jordan"],
           ["A. Norway", "B. Croatia", "C. Portugal", "D. Spain"],
           ["A. England", "B. Vatican City", "C. Russsia", "D. Thailand"]]

Answers = ("B","C","C","D","A")

guesses = []
score = 0
question_num = 0


for i in Questions:
    print("---------------------")
    print(i)
    for j in Options[question_num]:
        print(j)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == Answers[question_num]:
        score = score+1
        print("CORRECT")
    else:
        print("INCORRECT")
        print("The correct answer is ", Answers[question_num])
        
    question_num = question_num + 1

print("Your Total correct guesses: ", score)
