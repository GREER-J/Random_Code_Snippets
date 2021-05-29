from tkinter import *

question = ['One', 'Two', 'Three']
counter = 0

def main():
    root = Tk()
    root.title('Main')
    w = Label(root, text = "Welcome to the spelling test!")
    w.pack()
    One = Button(root, text = "Start the quiz", command = quiz)
    One.pack()

    Two = Button(root, text = "View the questions")
    Two.pack()

    Three = Button(root, text = "Edit the questions")
    Three.pack()

    root.mainloop()


def quiz():
    quiz = Tk()
    quiz.title('Quiz')
    w = Label(quiz, text = "Welcome to the quiz")
    w.pack()
    One = Button(quiz, text = "Instructions")
    One.pack()

    Two = Button(quiz, text = "Play", command = askQuestion)
    Two.pack()

    quiz.mainloop()

def getQuestion():
    global counter
    counter +=1
    return(question[counter-1])


def askQuestion():
    question = Tk()
    question.title('Question '+ str(counter +  1))
    w = Label(question, text = getQuestion())
    w.pack(side = TOP)
    w1 = Label(question, text = "Answer:")
    w1.pack(side = LEFT)
    e = Entry(question)
    e.pack(side = RIGHT)
    
    B = Button(question, text = "Next", command = askQuestion)
    B.pack(side = BOTTOM)

main()
