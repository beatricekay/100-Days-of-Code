from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create a list containing objects being initialized each with a question and an answer
# question = Question(text, answer)

question_bank = [Question(dict["text"], dict["answer"]) for dict in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

