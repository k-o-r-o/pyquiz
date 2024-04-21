import random
from question import Question

class Matching(Question):
    def __init__(self, qText, questionsAndMatches, allOrNothing, p):
        if not qText:
            print("Error: Invalid question text provided.")
            exit()
        if not isinstance(questionsAndMatches, list) or not all(len(pair) == 2 for pair in questionsAndMatches):
            print("Error: questionsAndMatches must have only two columns.")
            exit()

        formatted_qText = f"{qText}\n" + "\n".join(f"{i+1}){question}" for i, (question, _) in enumerate(questionsAndMatches))
        formatted_qText += "\nOptions: " + ", ".join(random.sample([match for _, match in questionsAndMatches], len(questionsAndMatches)))
        
        super().__init__(formatted_qText, p)
        self._matchingQuestions = questionsAndMatches
        self._allOrNothing = allOrNothing

    def getScore(self, answer):
        if not isinstance(answer, list) or len(answer) != len(self._matchingQuestions):
            return 0
        correct_matches = sum(1 for i, correct in enumerate([match for _, match in self._matchingQuestions])
                              if answer[i].strip().lower() == correct.lower())
        if self._allOrNothing:
            return self._points if correct_matches == len(self._matchingQuestions) else 0
        else:
            return self._points * (correct_matches / len(self._matchingQuestions))

    def __str__(self):
        base_str = super().__str__()
        all_or_nothing_str = "True" if self._allOrNothing else "False"
        return f"Matching:\nPoints: {self._points}\nAll or Nothing: {all_or_nothing_str}\n{base_str}"
