# ask the questions
# check if answer was correct
# check if at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list 
        self.score = 0
        # attribute = question_list
        # parameter = q_list

    # Returns True if there are still questions to load from the question bank
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    # Loads the next question from the question bank
    def next_question(self): 
        # Taking the first question OBJECT from the question bank
        current_question = self.question_list[self.question_number]
        
        # Here, current_question is a question OBJECT and we can use .text before text is an attribute
        # that belongs to a question OBJECT
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        
        # Calls the next method within the current method
        # Pass the user_answer and correct answer to the check_answer() method
        self.check_answer(user_answer, current_question.answer)

    # Checks if the user answer is the same as the correct answer
    # Receives the parameters from the next_question() method
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
