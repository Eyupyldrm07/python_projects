#  Question 

class Question:
    def __init__(self, text,chocies,answer):
        self.text = text
        self.choices =  chocies
        self.answer=answer
    
    def checkAnswer(self,answer):
        return self.answer == answer


# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex =0


    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self): 
        question = self.getQuestion()
        print(f'soru {self.questionIndex+1} : {question.text}')

        for q in question.choices:
            print('-'+q)

        answer = input('cevap')
        self.quess(answer)
        self.LoadQuestion()

    def quess(self,answer):
        question =self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex += 1


        


    def LoadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print('Score:',self.score)
    
    def displayProgress(self):
        totalQuestion =len(self.questions)
        questionNumber =self.questionIndex+1

        if questionNumber>totalQuestion:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))




q1 = Question('en iyi programlama dili hangiosidir ?',['c#','python','javascript','java'],'python')
q2 = Question('en populer programlama dili hangiosidir ?',['python','c#','javascript','java'],'python')
q3 = Question('en cok kazandiran programlama dili hangiosidir ?',['java','python','javascript','c#'],'python')
q4 = Question('en cok sevilen programlama dili hangiosidir ?',['java','python','javascript','c#'],'python')
q5 = Question('en kolay programlama dili hangiosidir ?',['java','python','javascript','c#'],'python')



questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.LoadQuestion()