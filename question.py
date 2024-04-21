from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, qText, p):
        if not qText:
            print("Error: Empty question text provided. Aborting creation of Question.")
            exit()
        if not isinstance(p, int) or p < 1:
            print("Error: Invalid points awarded to question. Aborting creation of Question.")
            exit()
        
        self._questionText = qText
        self._points = p

    def setQuestion(self, qText):
        self._questionText = qText
        
    def getQuestion(self):
        return self._questionText
    
    def setPoints(self, p):
        self._points = p

    def getPoints(self):
        return self._points

    @abstractmethod
    def getScore(self, answer):
        pass

    def __str__(self):
        return self._questionText

