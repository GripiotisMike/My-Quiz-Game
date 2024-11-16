from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank using list comprehension
question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

# Initialize the quiz and start asking questions
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
