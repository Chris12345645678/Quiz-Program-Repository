from tkinter import *
from random import*
import tkinter as tk

possible_question = []

text = open("questions1.txt", "r")
for line in text.readlines():
    possible_question.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4]])
   
            
class Questions:
    def __init__(self, parent):

        self.frame0 = LabelFrame(parent, height = 300)
        self.frame0.grid(row=0, column = 0)
 
        self.TitleLabel = Label(self.frame0, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "General Knowledge Quiz's", font= ("Times", "25", "bold"))
        self.TitleLabel.grid(columnspan = 5)
                             
        self.Quiz_One = Button(self.frame0, text = "Geography", padx = 33, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.Next_Question)   
        self.Quiz_One.grid(row = 6, column = 2)

        self.Quiz_Two = Button(self.frame0, text = "Famous People", padx = 21, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.Next_Question)   
        self.Quiz_Two.grid(row = 7, column = 2)

        self.Quiz_Three = Button(self.frame0, text = "National Dishes", padx = 21, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.Next_Question)   
        self.Quiz_Three.grid(row = 8, column = 2)

        self.frame1 = LabelFrame(parent, height = 300)

        self.TitleLabel = Label(self.frame1, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "", font= ("Times", "25", "bold"))
        self.TitleLabel.grid(columnspan = 5)

        self.Question_Label = Label(self.frame1, padx = 20, font =("bold", "14"), pady= 10)
        self.Question_Label.grid(row = 3, columnspan = 5)                        
        
        self.Answer_label1 = Button(self.frame1, text = "")
        self.Answer_label1.grid(row = 4, column = 0)
        
        self.Answer_label2 = Button(self.frame1, text = "")
        self.Answer_label2.grid(row = 4, column = 1)        
        
        self.Answer_label3 = Button(self.frame1, text = "")
        self.Answer_label3.grid(row = 4, column = 2)      
        
        self.Answer_label4 = Button(self.frame1, text = "")
        self.Answer_label4.grid(row = 4, column = 3)              
        

    def Next_Question(self):
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        q = randrange(len(possible_question))
        for i in possible_question[q]:
            current_question.append(i)
        possible_question.pop(q)
        self.answer.set(current_question[1])
        self.TitleLabel.configure(text = "Geography Quiz")
        self.Answer_label1.configure(text = current_question[1] ,padx = 20, pady = 10, command = lambda: self.Check_Answer(current_question[1]))
        self.Answer_label2.configure(text = current_question[2] ,padx = 20, pady = 10, command = lambda: self.Check_Answer(current_question[2]))
        self.Answer_label3.configure(text = current_question[3] ,padx = 20, pady = 10, command = lambda: self.Check_Answer(current_question[3]))
        self.Answer_label4.configure(text = current_question[4] ,padx = 20, pady = 10, command = lambda: self.Check_Answer(current_question[4]))


        self.Question_Label.configure(text = current_question[0])

        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)

    def Check_Answer(self, Answer):
        if self.answer.get() == Answer:
            self.Next_Question()
            print("Correct!")
        else:
            self.Next_Question()
            print("Incorrect!")
        



if __name__ == "__main__":
    root = Tk()
    frames = Questions(root)
    root.title("Quiz")
    root.mainloop()