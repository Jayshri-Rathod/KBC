from tkinter import *
from tkinter.font import BOLD, ITALIC
from random import randint
window = Tk()
label=Label(window,font=("Arial",50,BOLD),text="WELCOME TO KON BANEGA CROREPATI",fg="black")
label.pack()
window.configure(bg="grey")
window.geometry('100x100')
img=PhotoImage(file="/home/jayshri/Downloads/jayshri.png")
image_list=[img]
pick_number=randint(0,0)
image_label=Label(image=image_list[pick_number])
image_label.pack(pady=70)


class Question:
    def __init__(self, question,answers,correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, font=("Arial",20,BOLD),text="Right! You Won Rs/ 1000",fg="dark blue")
            right += 1
        else:
            label = Label(view,font=("Arial",20,BOLD) ,text="Wrong! You lose Rs/ 1000",fg="dark blue")
            # window.destroy()
        label.pack() 
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view,font=("Arial",30,BOLD), text=self.question,fg="black").pack()
        Radiobutton(view, font=("Arial",20,BOLD),text=self.answers[0],width=25,command=lambda *args: self.check("A", view),bg="grey",fg="dark red").pack()
        Radiobutton(view, font=("Arial",20,BOLD),text=self.answers[1],width=25,command=lambda *args: self.check("B", view),bg="grey",fg="dark red").pack()
        Radiobutton(view, font=("Arial",20,BOLD),text=self.answers[2],width=25,command=lambda *args: self.check("C", view),bg="grey",fg="dark red").pack()
        Radiobutton(view, font=("Arial",20,BOLD),text=self.answers[3],width=25,command=lambda *args: self.check("D", view),bg="grey",fg="dark red").pack()
        return view


    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window,font=("Arial",30,BOLD),text="Thank you for answering the questions. " + str(right) + " of " +str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)
         
button = Button(window,font=("Arial",20,BOLD),bd=10,height=2,width=6,text= "START", command=askQuestion,bg="light blue",fg="black")
button.pack()



window.mainloop()