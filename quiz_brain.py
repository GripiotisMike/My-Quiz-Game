class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are more questions to ask."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Displays the next question and checks the answer."""
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        valid_answer = False
        
        while not valid_answer:
            ua = input(f"Q.{self.question_number}: {current_q.text}  (True/False): ").strip().lower()
            if ua in ['true', 'false']:
                valid_answer = True
            else:
                print("Please enter 'True' or 'False'.")
                
        self.check_answer(ua, current_q.answer)

    def check_answer(self, ua, correct_answer):
        """Checks if the answer is correct and updates the score."""
        if ua == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
