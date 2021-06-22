from tkinter import *
from random import*
import tkinter as tk

possible_question1 = []
possible_question2 = []
possible_question3 = []

text1 = open("geography_questions.txt", "r")
for line in text1.readlines():
    possible_question1.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4], line.split(",")[5]])
   
text2 = open("celebrities_questions.txt", "r")
for line in text2.readlines():
    possible_question2.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4]])
        
text3 = open("dishes_questions.txt", "r")
for line in text3.readlines():
    possible_question3.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4], line.split(",")[5]])
            
class Questions:
    def __init__(self, parent):

        self.frame0 = LabelFrame(parent, height = 300)
        self.frame0.grid(row=0, column = 0)
 
        self.title_label = Label(self.frame0, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "General Knowledge Quiz's", font= ("Times", "25", "bold"))
        self.title_label.grid(row=1, columnspan = 5)
                             
        self.blank = Label(self.frame0)                    
        self.blank.grid(row=2)
                           
        self.quiz_one = Button(self.frame0, text = "Geography", padx = 33, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.next_question_geography)   
        self.quiz_one.grid(row = 3, column = 2)

        self.quiz_two = Button(self.frame0, text = "Celebrities", padx = 33, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.next_question_celebrities)   
        self.quiz_two.grid(row = 4, column = 2)

        self.quiz_three = Button(self.frame0, text = "National Dishes", padx = 21, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.next_question_dishes)   
        self.quiz_three.grid(row = 5, column = 2)
        
        self.blank = Label(self.frame0)                    
        self.blank.grid(row=6)        

        self.frame1 = LabelFrame(parent, height = 300)

        self.title_label = Label(self.frame1, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "", font= ("Times", "25", "bold"))
        self.title_label.grid(columnspan = 5)

        self.question_label = Label(self.frame1, font =("bold", "23"), pady = 10)
        self.question_label.grid(row = 3, columnspan = 5)  
        
        self.image_option = PhotoImage()
        
        self.image_label = Label(self.frame1, width= 390, height = 200, image = self.image_option)
        self.image_label.grid(row = 4, columnspan = 5)
        
        self.answer_label1 = Button(self.frame1, font =("bold", "20"), text = "")
        self.answer_label1.grid(row = 5, column = 1)
        
        self.answer_label2 = Button(self.frame1, font =("bold", "20"), text = "")
        self.answer_label2.grid(row = 5, column = 2)        
        
        self.answer_label3 = Button(self.frame1, font =("bold", "20"), text = "")
        self.answer_label3.grid(row = 6, column = 1)      
        
        self.answer_label4 = Button(self.frame1, font =("bold", "20"), text = "")
        self.answer_label4.grid(row = 6, column = 2)              
        

    def next_question_geography(self):
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        q = randrange(len(possible_question1))
        for i in possible_question1[q]:
            current_question.append(i)
        possible_question1.pop(q)
        self.answer.set(current_question[1])
        self.title_label.configure(text = "Geography Quiz")
        self.answer_label1.configure(text = current_question[1] ,width = 15, height = 3, command = lambda: self.check_answer_geography(current_question[1]))
        self.answer_label2.configure(text = current_question[2] ,width = 15, height = 3, command = lambda: self.check_answer_geography(current_question[2]))
        self.answer_label3.configure(text = current_question[3] ,width = 15, height = 3, command = lambda: self.check_answer_geography(current_question[3]))
        self.answer_label4.configure(text = current_question[4] ,width = 15, height = 3, command = lambda: self.check_answer_geography(current_question[4]))

        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "What is the capital city of {}".format(current_question[5]))

        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)
        

    def next_question_celebrities(self):
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        q = randrange(len(possible_question2))
        for i in possible_question2[q]:
            current_question.append(i)
        possible_question2.pop(q)
        self.answer.set(current_question[1])
        self.title_label.configure(text = "Celebrities Quiz")
        self.answer_label1.configure(text = current_question[1] ,width= 15, height = 3, command = lambda: self.check_answer_celebrities(current_question[1]))
        self.answer_label2.configure(text = current_question[2] ,width= 15, height = 3, command = lambda: self.check_answer_celebrities(current_question[2]))
        self.answer_label3.configure(text = current_question[3] ,width= 15, height = 3, command = lambda: self.check_answer_celebrities(current_question[3]))
        self.answer_label4.configure(text = current_question[4] ,width= 15, height = 3, command = lambda: self.check_answer_celebrities(current_question[4]))
        
        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "Who is this?")
        
        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)


    def next_question_dishes(self):
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        q = randrange(len(possible_question3))
        for i in possible_question3[q]:
            current_question.append(i)
        possible_question3.pop(q)
        self.answer.set(current_question[1])
        self.title_label.configure(text = "National Dishes Quiz")
        self.answer_label1.configure(text = current_question[1] ,width= 15, height = 3, command = lambda: self.check_answer_dishes(current_question[1]))
        self.answer_label2.configure(text = current_question[2] ,width= 15, height = 3, command = lambda: self.check_answer_dishes(current_question[2]))
        self.answer_label3.configure(text = current_question[3] ,width= 15, height = 3, command = lambda: self.check_answer_dishes(current_question[3]))
        self.answer_label4.configure(text = current_question[4] ,width= 15, height = 3, command = lambda: self.check_answer_dishes(current_question[4]))

        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "Where is the dish {} from?".format(current_question[5]))
        
        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)



    def check_answer_geography(self, Answer):
        if self.answer.get() == Answer:
            self.next_question_geography()
            print("Correct")
        else:
            self.next_question_geography()
            print("Incorrect")
        
    def check_answer_celebrities(self, Answer):
        if self.answer.get() == Answer:
            self.next_question_celebrities()
            print("Correct")
        else:
            self.next_question_celebrities()
            print("Incorrect")

    def check_answer_dishes(self, Answer):
        if self.answer.get() == Answer:
            self.next_question_dishes()
            print("Correct")
        else:
            self.next_question_dishes()
            print("Incorrect")
        
        

if __name__ == "__main__":
    root = Tk()
    frames = Questions(root)
    root.title("Quiz")
    root.mainloop()