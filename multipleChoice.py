from choice import Choice  
from question import Question

class MultipleChoice(Question):
    def __init__(self, qText, choiceText, p, answer):
        if not qText:
            print("Error: Empty question text provided. Aborting creation of Question.")
            exit()
        if not isinstance(choiceText, list) or len(choiceText) != 4:
            print("Error: Choice text must be a list containing 4 strings.")
            exit()

        formatted_qText = f"{qText}\nA. {choiceText[0]}\nB. {choiceText[1]}\nC. {choiceText[2]}\nD. {choiceText[3]}"
        super().__init__(formatted_qText, p)
        self._correctAnswer = answer

    def setCorrectAnswer(self, answer):
        if answer in Choice.__members__:
            self._correctAnswer = Choice[answer]
        else:
            print("Error: Invalid choice provided. Must be 'A', 'B', 'C', or 'D'.")

    def getCorrectAnswer(self):
        return self._correctAnswer.name

    def getScore(self, answer):
        if answer and len(answer) > 0:
            cleaned_answer = answer[0].strip().upper()
            if cleaned_answer and len(cleaned_answer) > 0:
                user_choice = Choice[cleaned_answer[0]] if cleaned_answer[0] in Choice.__members__ else None
                return self._points if user_choice == self._correctAnswer else 0
        return 0

    def __str__(self):
        base_str = super().__str__()
        return f"Multiple Choice:\nPoints: {self._points}\n{base_str}"