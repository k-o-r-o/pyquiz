from trueFalse import TrueFalse
from fillInBlank import FillInBlank
from multipleChoice import MultipleChoice
from matching import Matching
from quiz import Quiz
from choice import Choice

def parse_question(data):
    """ Parse individual question blocks and return the appropriate question object. """
    lines = [line.strip() for line in data if line.strip()]  
    question_type = lines[0]
    points = int(lines[1].split(":")[1].strip())
    qText = lines[2].strip().strip('"')

    if question_type == 'True or False':
        correct_answer = lines[3].strip().strip('"') == 'True'
        return TrueFalse(qText, points, correct_answer)
    elif question_type == 'Fill in Blank':
        parts = lines[2].strip('"').split('", "')
        answers = lines[3].strip('"').split('", "')
        return FillInBlank(parts, points, answers)
    elif question_type == 'Multiple Choice':
        choices = lines[3].strip('"').split('", "')
        correct_choice = lines[4].strip().strip('"')  
        return MultipleChoice(qText, choices, points, Choice[correct_choice])
    elif question_type == 'Matching':
        allOrNothing = lines[2].split(":")[1].strip() == 'True'
        items = lines[3].strip('"').split('", "')
        matches = lines[4].strip('"').split('", "')
        questionsAndMatches = list(zip(items, matches))
        return Matching(qText, questionsAndMatches, allOrNothing, points)

    
def read_quiz(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split("\n\n")  
    questions = []
    for block in content:
        question_data = block.split("\n")
        question = parse_question(question_data)
        questions.append(question)
    print(f"Loaded {len(questions)} questions.")  
    return Quiz(questions)

def take_quiz(quiz):
    """ Administer the quiz, collect responses, and calculate scores. """
    total_score = 0
    max_score = 0
    for question in quiz: 
        print(question)
        response = input("Your answer: ").split(", ") 
        score = question.getScore(response)
        total_score += score
        max_score += question.getPoints()
        print(f"Scored: {score}/{question.getPoints()}\n")
    print(f"Total Score: {total_score}/{max_score} ({(total_score/max_score)*100:.2f}%)")

if __name__ == "__main__":
    quiz = read_quiz('quiz.txt')
    take_quiz(quiz)
