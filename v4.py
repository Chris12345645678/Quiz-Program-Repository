from tkinter import *
from random import*
import tkinter as tk
import random

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
        self.frame0.grid(row = 0, column = 0)
        
        self.score = 0           
        self.count = 0          

        self.title_label1 = Label(self.frame0, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "General Knowledge Quiz's", font = ("Times", "25", "bold"))
        self.title_label1.grid(row = 1, columnspan = 5)
                             
        self.blank = Label(self.frame0)                    
        self.blank.grid(row = 2)
                           
        self.quiz1 = Button(self.frame0, text = "Geography", padx = 33, font = ("bold", "11"), bg = "white", pady = 10, anchor = W, command = self.next_question_geography)   
        self.quiz1.grid(row = 3, column = 2)

        self.quiz2 = Button(self.frame0, text = "Celebrities", padx = 33, font = ("bold", "11"), bg = "white", pady = 10, anchor = W, command = self.next_question_celebrities)   
        self.quiz2.grid(row = 4, column = 2)

        self.quiz3 = Button(self.frame0, text = "National Dishes", padx = 21, font = ("bold", "11"), bg = "white", pady = 10, anchor = W, command = self.next_question_dishes)   
        self.quiz3.grid(row = 5, column = 2)
        
        self.blank = Label(self.frame0)                    
        self.blank.grid(row = 6)           

        self.frame1 = LabelFrame(parent, height = 300)

        self.title_label2 = Label(self.frame1, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "", font = ("Times", "25", "bold"))
        self.title_label2.grid(columnspan = 5)

        self.question_label = Label(self.frame1, font = ("bold", "23"), pady = 10)
        self.question_label.grid(row = 3, columnspan = 5)  
        
        self.image_option = PhotoImage()
        
        self.image_label = Label(self.frame1, width= 390, height = 200, image = self.image_option)
        self.image_label.grid(row = 4, columnspan = 5)
        
        self.answer_label1 = Button(self.frame1, font = ("bold", "20"), text = "")
        self.answer_label1.grid(row = 5, column = 1)
        
        self.answer_label2 = Button(self.frame1, font = ("bold", "20"), text = "")
        self.answer_label2.grid(row = 5, column = 2)        
        
        self.answer_label3 = Button(self.frame1, font = ("bold", "20"), text = "")
        self.answer_label3.grid(row = 6, column = 1)      
        
        self.answer_label4 = Button(self.frame1, font = ("bold", "20"), text = "")
        self.answer_label4.grid(row = 6, column = 2)              
        
        self.frame2 = LabelFrame(parent, height = 300)
            
        self.title_label3 = Label(self.frame2, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Scoreboard", font = ("Times", "25", "bold"))
        self.title_label3.grid(columnspan = 5)            
            
        self.home = Button(self.frame2, text = "Home", padx = 33, font = ("bold", "11"), bg = "white", pady = 10, anchor = W, command = self.home_screen)   
        self.home.grid(row = 3, column = 2)         
        
        
    def next_question_geography(self):
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        q = randrange(len(possible_question1))
        for i in possible_question1[q]:
            current_question.append(i)
        possible_question1.pop(q)
        self.answer.set(current_question[1])
        
        self.title_label2.configure(text = "Geography Quiz")
        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "What is the capital city of {}".format(current_question[5]))
        
        current_question.pop(5)
        current_question.pop(0)
        
        randomised_question = []
        while 4 > len(randomised_question):
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])
                
        self.answer_label1.configure(text = randomised_question[0] ,width = 15, height = 3, command = lambda: self.check_answer_geography(randomised_question[0]))
        self.answer_label2.configure(text = randomised_question[1] ,width = 15, height = 3, command = lambda: self.check_answer_geography(randomised_question[1]))
        self.answer_label3.configure(text = randomised_question[2] ,width = 15, height = 3, command = lambda: self.check_answer_geography(randomised_question[2]))
        self.answer_label4.configure(text = randomised_question[3] ,width = 15, height = 3, command = lambda: self.check_answer_geography(randomised_question[3]))
                      
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
        
        self.title_label2.configure(text = "Celebrities Quiz")
        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "Who is this Celebrity?")   
        
        current_question.pop(0)   
        
        randomised_question = []
        while 4 > len(randomised_question):
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])        
        
        self.answer_label1.configure(text = randomised_question[0] ,width = 15, height = 3, command = lambda: self.check_answer_celebrities(randomised_question[0]))
        self.answer_label2.configure(text = randomised_question[1] ,width = 15, height = 3, command = lambda: self.check_answer_celebrities(randomised_question[1]))
        self.answer_label3.configure(text = randomised_question[2] ,width = 15, height = 3, command = lambda: self.check_answer_celebrities(randomised_question[2]))
        self.answer_label4.configure(text = randomised_question[3] ,width = 15, height = 3, command = lambda: self.check_answer_celebrities(randomised_question[3]))
        
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
        
        self.title_label2.configure(text = "National Dishes Quiz")
        self.image_option.configure(file = current_question[0])
        self.question_label.configure(text = "Where is the dish {} from?".format(current_question[5])) 
        
        current_question.pop(5)
        current_question.pop(0)        
        
        randomised_question = []
        while 4 > len(randomised_question):
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])        
        
        self.answer_label1.configure(text = randomised_question[0] ,width = 15, height = 3, command = lambda: self.check_answer_dishes(randomised_question[0]))
        self.answer_label2.configure(text = randomised_question[1] ,width = 15, height = 3, command = lambda: self.check_answer_dishes(randomised_question[1]))
        self.answer_label3.configure(text = randomised_question[2] ,width = 15, height = 3, command = lambda: self.check_answer_dishes(randomised_question[2]))
        self.answer_label4.configure(text = randomised_question[3] ,width = 15, height = 3, command = lambda: self.check_answer_dishes(randomised_question[3]))

        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)
    
    
    def end_screen(self):
        self.frame1.grid_remove()
        self.frame2.grid()
        
        
    def home_screen(self):
        self.frame2.grid_remove()         
        self.frame0.grid()
        self.score = 0  
        self.count = 0         
    

    def check_answer_geography(self, Answer):
        if self.answer.get() == Answer:
            self.score += 1
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))            
        else:
            self.score += 0
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))            
            
        if self.count > 4:
            self.end_screen()
            self.scoreboard = Label(self.frame2,text = "You Scored {} out of 5".format(self.score))
            self.scoreboard.grid(columnspan = 5, row = 2)      
        else:
            self.next_question_geography()
                     
            
    def check_answer_celebrities(self, Answer):
        if self.answer.get() == Answer:
            self.score += 1
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))            
        else:
            self.score += 0
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))                
                
        if self.count > 4:
            self.end_screen()
            self.scoreboard = Label(self.frame2,text = "You Scored {} out of 5".format(self.score))
            self.scoreboard.grid(columnspan = 5, row = 2)      
        else:
            self.next_question_celebrities()
        
        
    def check_answer_dishes(self, Answer):
        if self.answer.get() == Answer:
            self.score += 1
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))
        else:
            self.score += 0
            self.count +=1
            print("score = {}".format(self.score))
            print("count = {}".format(self.count))            
                
        if self.count > 4:
            self.end_screen()
            self.scoreboard = Label(self.frame2,text = "You Scored {} out of 5".format(self.score))
            self.scoreboard.grid(columnspan = 5, row = 2)      
        else:        
            self.next_question_dishes()


if __name__ == "__main__":
    root = Tk()
    frames = Questions(root)
    root.title("Quiz")
    root.mainloop()