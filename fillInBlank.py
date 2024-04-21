from question import Question
class FillInBlank(Question):
    def __init__(self, qText, p, answer):
        if qText is None or answer is None:
            print("Error: None reference provided for question text or answer.")
            exit()

        if len(qText) - 1 != len(answer):
            print("Error: Mismatch between number of question parts and answers.")
            exit()

        formatted_qText = ' ______ '.join(qText)
        super().__init__(formatted_qText, p)

        self._numBlanks = len(qText) - 1
        self._correctAnswer = [ans.lower().replace(" ", "") for ans in answer]

    def setCorrectAnswer(self, answer):
        if len(answer) == self._numBlanks:
            self._correctAnswer = [ans.lower().replace(" ", "") for ans in answer]
        else:
            print("Error: Incorrect number of answers provided.")

    def getCorrectAnswer(self):
        return self._correctAnswer

    def getScore(self, answer):
        score = 0
        if len(answer) == self._numBlanks:
            score = sum(1 for i, ans in enumerate(answer) if ans.lower().replace(" ", "") == self._correctAnswer[i])
        return self._points * (score / self._numBlanks)

    def __str__(self):
        base_str = super().__str__()
        return f"Fill in Blank:\nPoints: {self._points}\n{base_str}"
