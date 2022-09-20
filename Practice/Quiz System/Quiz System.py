def MyQuizSystem():
    questions_txt = open("Practice\Quiz System\questions.txt", 'r')
    questions_answers = [line.strip() for line in questions_txt.readlines()]
    questions_txt.close()


    questions = []
    answers = []
    n = 0
    m = 3


    for line in questions_answers:
        questions_answers = line.split('=')
        questions.append(questions_answers[0])
        answers.append(int(questions_answers[1]))


    for i in range(0, len(questions_answers) + 1):
        user_input = int(input(f"What is {questions[i]}="))
        if(user_input == answers[i]): # Never correct for some reason...
            n = n + 1


    results = open("Practice\Quiz System\\results.txt", 'w')
    results.write(f"Your final score is {n}/{m}")
    results.close()


def TheirQuizSystem():
    questions = open("Practice\Quiz System\questions.txt", "r")  # read from questions.txt
 
    question_list = [line.strip() for line in questions]
    questions.close()
 
    score = 0  # initialize score
    total = len(question_list)  # set total score
 
    # This for loop here is very efficent. I used 2 for loops in my version
    # that did the same as this 1. Very inefficient...
    for line in question_list:
        q, a = line.split("=")
 
        ans = input(f"{q}=")
 
        if a == ans:  # if user input matches answer
            score += 1  # increase score
 
    result = open("Practice\Quiz System\\results.txt", "w")  # open result.txt
    result.write(f"Your final score is {score}/{total}.")
    result.close()

