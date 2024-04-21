from question import Question
class Quiz:
    def __init__(self, qList=[]):
        if not all(isinstance(q, Question) for q in qList):
            print("Error: qList must contain only instances of the Question class.")
            self.questions = []
        else:
            self.questions = qList

    def addQuestion(self, question):
        if not isinstance(question, Question):
            print("Error: You may only add instances of the Question class")
        else:
            self.questions.append(question)

    def __add__(self, quiz02):
        if not isinstance(quiz02, Quiz):
            raise ValueError("Operand must be an instance of Quiz")
        return Quiz(self.questions + quiz02.questions)

    def __len__(self):
        return len(self.questions)

    def getTotalPoints(self):
        return sum(question.getPoints() for question in self.questions)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.questions):
            question = self.questions[self._index]
            self._index += 1
            return question
        else:
            raise StopIteration()
