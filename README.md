# True/False Quiz Game
A simple True/False quiz game built in Python. The game fetches questions about video games and quizzes the user, keeping track of their score as they answer each question. This project demonstrates the use of object-oriented programming (OOP) in Python and organizes the code into multiple files for modularity.

- In this Project I learned how to create Classes and add Methods to them.

- I also learned how to work with Attributes, Class Constructors and the __init__() Function.

## Files
- data.py: Contains a list of quiz questions and their correct answers.
- main.py: The entry point of the quiz game that runs the game logic.
- question_model.py: Defines the Question class that holds the question text and answer.
- quiz_brain.py: Contains the QuizBrain class, which manages the quiz logic (question tracking, scoring, etc.).

## Features
- Multiple Question Categories: The quiz questions are focused on video games, but can easily be modified to add more categories.
- Real-time Feedback: After each question, the user is shown whether their answer was correct or incorrect, along with the correct answer and their current score.
- Score Tracking: The score is tracked throughout the game, and at the end, the user’s final score is displayed.
