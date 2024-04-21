from question import Question
class TrueFalse(Question):
    def __init__(self, qText, p, answer):
        super().__init__(qText, p)
        self._correctAnswer = bool(answer)

    def setCorrectAnswer(self, answer):
        self._correctAnswer = answer
        
    def getCorrectAnswer(self):
        return self._correctAnswer

    def getScore(self, answer):
        if answer:
            user_answer = answer[0].strip().lower() == 'true'
            if user_answer == self._correctAnswer:
                return self._points
            else:
                return 0
        else:
            return 0

    def __str__(self):
        base_str = super().__str__()
        formatted_str = "True or False:\nPoints: " + str(self._points) + "\n" + base_str
        return formatted_str
