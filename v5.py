from tkinter import * 
from random import* 
import tkinter as tk
import random

#defining lists
possible_question1 = [] #defining geography list
possible_question2 = [] #defining celebrities list
possible_question3 = [] #defining national dishes list

#defining constants
BG = "white" #primary background colour
BG2 = "plum" #secondary background colour
FG = "black" #text colour
FT = "bold", "20" #text attributes for buttons
FT2 = "Times", "25", "bold" #text attributes for page title's
FT3 = "bold", "23" #text attributes for questions
W = "15" #width for buttons
W2 = "27" #width for title's
H = "3" #height for buttons 
PX = "30" #padx for title's
PY = "10" #pady for title's
PY2 = "5" #pady for score statement


text1 = open("geography_questions.txt", "r") #opening geography text file in "read" mode
for line in text1.readlines(): #turning text file into a list
    possible_question1.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4], line.split(",")[5]]) 
   
text2 = open("celebrities_questions.txt", "r") #opening celebrities text file in "read" mode
for line in text2.readlines(): #turning text file into a list
    possible_question2.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4]]) 
        
text3 = open("dishes_questions.txt", "r") #opening national dishes text file in "read" mode
for line in text3.readlines(): #turning text file into a list
    possible_question3.append([line.split(",")[0], line.split(",")[1], line.split(",")[2],line.split(",")[3], line.split(",")[4], line.split(",")[5]]) 
     
     
class Transition: #defining support class which contains transition functions
    def end_transition(self): #defining function which moves user to scoreboard screen after questions are complete
        self.quiz_screen.grid_remove() #removing quiz screen
        self.scoreboard_screen.grid() #opening scoreboard screen
        
    def home_transition(self): #defining function which moves user to home screen from scoreboard screen
        self.scoreboard_screen.grid_remove() #removing scoreboard screen          
        self.home_screen.grid() #opening home screen
        self.score = 0 #resetting score variable to 0           
        self.count = 0 #resetting count variable to 0          
        
            
class Questions: #defining the main (parent) class
    def __init__(self, parent): #defining constructor that initializes the attributes of the class
        self.home_screen = LabelFrame(parent, bg = BG) #creating first frame
        self.home_screen.grid(row = 0, column = 0)
        
        self.score = 0 #setting score variable to 0           
        self.count = 0 #setting count variable to 0          

        self.title_label1 = Label(self.home_screen, text = "General Knowledge Quizzes", bg = BG2, fg = FG, font = FT2, padx = PX, pady = PY, width = W2) #creating title label for first frame and giving it attriubutes
        self.title_label1.grid(row = 1, columnspan = 5) #positioning title label 
         
        self.intro_label = Label(self.home_screen, text = "⊱ ─────────────── ⊰", bg = BG, fg = FG, font = FT3) #creating top divider and giving it attributes 
        self.intro_label.grid(row = 2, columnspan = 5) #positioning top divder
                                 
        self.intro = Label(self.home_screen, text = "What subject would you like\nto be tested on today?", bg = BG, fg = FG, font = FT3, pady = 4) #creating menu question and giving it attributes
        self.intro.grid(row = 3, columnspan = 5) #positioning menu question
            
        self.blank = Label(self.home_screen) #creating blank space for aesthetic appeal                     
        self.blank.grid(row = 4) #positioning blank space           
                                                                      
        self.quiz1 = Button(self.home_screen, text = "Geography", bg = BG, fg = FG, font = FT, width = W, height = H, command = self.next_question_geography) #creating geography quiz button
        self.quiz1.grid(row = 5, column = 2) #positioning button

        self.quiz2 = Button(self.home_screen, text = "Celebrities", bg = BG, fg = FG, font = FT, width = W, height = H, command = self.next_question_celebrities) #creating celebrities quiz button
        self.quiz2.grid(row = 6, column = 2) #positioning button

        self.quiz3 = Button(self.home_screen, text = "National Dishes", bg = BG, fg = FG, font = FT, width = W, height = H, command = self.next_question_dishes) #creating national dishes quiz button  
        self.quiz3.grid(row = 7, column = 2) #positioning button 
        
        self.blank = Label(self.home_screen) #creating blank space for aesthetic appeal                  
        self.blank.grid(row = 8) #positioning blank space           
        
        self.intro_label2 = Label(self.home_screen, text = "⊱ ─────────────── ⊰", bg = BG, fg = FG, font = FT3) #creating bottom divider and giving it attributes    
        self.intro_label2.grid(row = 10, columnspan = 5) #positioning bottom divder 
        
        self.quiz_screen = LabelFrame(parent, bg = BG) #creating second frame

        self.title_label2 = Label(self.quiz_screen, text = "", bg = BG2, fg = FG, font = FT2, padx = PX, pady = PY, width = W2) #creating title label for second frame and giving it attriubutes
        self.title_label2.grid(columnspan = 5) #positioning title label 

        self.question_label = Label(self.quiz_screen, bg = BG, fg = FG, font = FT3, pady = PY) #question label where questions are called depending on which quiz is chosen
        self.question_label.grid(row = 3, columnspan = 5) #positioning question label
        
        self.image_option = PhotoImage() #taking image from text file and storing as a variable
        
        self.image_label = Label(self.quiz_screen, width= 390, height = 200, image = self.image_option) #producing image and giving it attributes
        self.image_label.grid(row = 4, columnspan = 5) #positioning image
        
        self.answer_label1 = Button(self.quiz_screen, text = "", bg = BG, fg = FG, font = FT, width = W, height = H) #creating top left button
        self.answer_label1.grid(row = 5, column = 1) #positioning top left button
        
        self.answer_label2 = Button(self.quiz_screen, text = "", bg = BG, fg = FG, font = FT, width = W, height = H) #creating top right button
        self.answer_label2.grid(row = 5, column = 2) #positioning top right button      
        
        self.answer_label3 = Button(self.quiz_screen, text = "", bg = BG, fg = FG, font = FT, width = W, height = H) #creating bottom left button
        self.answer_label3.grid(row = 6, column = 1) #positioning bottom left button     
        
        self.answer_label4 = Button(self.quiz_screen, text = "", bg = BG, fg = FG, font = FT, width = W, height = H) #creating bottom right button
        self.answer_label4.grid(row = 6, column = 2) #positioning bottom right button             
        
        self.scoreboard_screen = LabelFrame(parent, bg = BG) #creating third frame
            
        self.title_label3 = Label(self.scoreboard_screen, text = "Scoreboard", bg = BG2, fg = FG, font = FT2, padx = PX, pady = PY, width = W2) #creating title label for third frame and giving it attriubutes
        self.title_label3.grid(columnspan = 5) #positioning title label     
        
        self.clap_image = PhotoImage(file = 'Pictures/clap.gif') #storing image as a variable
        self.clap_image_label = Label(self.scoreboard_screen, image = self.clap_image, width= 390, height = 283) #producing image and giving it attributes
        self.clap_image_label.grid(row = 3, columnspan = 5) #positioning image
        
        self.home = Button(self.scoreboard_screen, text = "Home", bg = BG, fg = FG, font = FT, width = W, height = H, command = lambda: Transition.home_transition(self)) #creating home button  
        self.home.grid(row = 4, column = 2) #positioning button        

        self.exit = Button(self.scoreboard_screen, text = "Exit", bg = BG, fg = FG, font = FT, width = W, height = H, command = parent.destroy) #creating exit button  
        self.exit.grid(row = 4, column = 3) #positioning button                   
                 
        
    def next_question_geography(self): #defining function which brings next question in geography quiz
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        r = randrange(len(possible_question1))
        for i in possible_question1[r]:
            current_question.append(i)
        possible_question1.pop(r)
        self.answer.set(current_question[1]) #setting second component of each line to the correct answer
        
        self.title_label2.configure(text = "Geography Quiz") #text which is displayed on second screen when user does the geography quiz
        self.image_option.configure(file = current_question[0]) #grabs image adress from start of text file line and configures to image
        self.question_label.configure(text = "What is the capital city of {}".format(current_question[5])) #question for second screen when user does the geography quiz
        
        current_question.pop(5) #removes question from list
        current_question.pop(0) #removes image from list
        
        randomised_question = [] #defining random question list
        while 4 > len(randomised_question): #randomises button position of answers
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])
                
        self.answer_label1.configure(text = randomised_question[0], command = lambda: self.check_answer_geography(randomised_question[0])) #appending answer 1 to top left button
        self.answer_label2.configure(text = randomised_question[1], command = lambda: self.check_answer_geography(randomised_question[1])) #appending answer 1 to top right button
        self.answer_label3.configure(text = randomised_question[2], command = lambda: self.check_answer_geography(randomised_question[2])) #appending answer 1 to bottom left button
        self.answer_label4.configure(text = randomised_question[3], command = lambda: self.check_answer_geography(randomised_question[3])) #appending answer 1 to bottom right button
                      
        self.home_screen.grid_remove() #removing home screen
        self.quiz_screen.grid() #opening quiz screen
        

    def next_question_celebrities(self): #defining function which brings next question in celebrities quiz
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        r = randrange(len(possible_question2))
        for i in possible_question2[r]:
            current_question.append(i)
        possible_question2.pop(r)
        self.answer.set(current_question[1]) #setting second component of each line to the correct answer
        
        self.title_label2.configure(text = "Celebrities Quiz") #text which is displayed on second screen when user does the celbrities quiz
        self.image_option.configure(file = current_question[0]) #grabs image adress from start of text file line and configures to image
        self.question_label.configure(text = "Who is this Celebrity?") #question for second screen when user does the celebrities quiz  
        
        current_question.pop(0) #removes image from list   
        
        randomised_question = [] #defining random question list
        while 4 > len(randomised_question): #randomises button position of answers
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])        
        
        self.answer_label1.configure(text = randomised_question[0], command = lambda: self.check_answer_celebrities(randomised_question[0])) #appending answer 1 to top left button
        self.answer_label2.configure(text = randomised_question[1], command = lambda: self.check_answer_celebrities(randomised_question[1])) #appending answer 1 to top right button
        self.answer_label3.configure(text = randomised_question[2], command = lambda: self.check_answer_celebrities(randomised_question[2])) #appending answer 1 to bottom left button
        self.answer_label4.configure(text = randomised_question[3], command = lambda: self.check_answer_celebrities(randomised_question[3])) #appending answer 1 to bottom right button
        
        self.home_screen.grid_remove() #removing home screen
        self.quiz_screen.grid() #opening quiz screen


    def next_question_dishes(self): #defining function which brings next question in national dishes quiz
        self.answer = StringVar()
        current_question = [""]
        current_question.clear()
        r = randrange(len(possible_question3))
        for i in possible_question3[r]:
            current_question.append(i)
        possible_question3.pop(r)
        self.answer.set(current_question[1]) #setting second component of each line to the correct answer
        
        self.title_label2.configure(text = "National Dishes Quiz") #text which is displayed on second screen when user does the national dishes quiz
        self.image_option.configure(file = current_question[0]) #grabs image adress from start of text file line and configures to image
        self.question_label.configure(text = "Where is the dish {} from?".format(current_question[5])) #question for second screen when user does the national dishes quiz
        
        current_question.pop(5) #removes question from list
        current_question.pop(0) #removes image from list     
        
        randomised_question = [] #defining random question list
        while 4 > len(randomised_question): #randomises button position of answers
            randomised_question.insert(0, random.choice(current_question))
            current_question.remove(randomised_question[0])        
        
        self.answer_label1.configure(text = randomised_question[0], command = lambda: self.check_answer_dishes(randomised_question[0])) #appending answer 1 to top left button
        self.answer_label2.configure(text = randomised_question[1], command = lambda: self.check_answer_dishes(randomised_question[1])) #appending answer 1 to top right button
        self.answer_label3.configure(text = randomised_question[2], command = lambda: self.check_answer_dishes(randomised_question[2])) #appending answer 1 to bottom left button
        self.answer_label4.configure(text = randomised_question[3], command = lambda: self.check_answer_dishes(randomised_question[3])) #appending answer 1 to bottom right button

        self.home_screen.grid_remove() #removing home screen
        self.quiz_screen.grid() #opening quiz screen
        

    def check_answer_geography(self, Answer): #defining function which checks answer for geography questions
        if self.answer.get() == Answer: #checks users answer against correct answer set in above function
            self.score += 1 #if answer is correct: score variable increases by 1
            self.count += 1 #if answer is correct: count variable increases by 1       
        else:
            self.score += 0 #if answer is incorrect: score variable increases by 0
            self.count += 1 #if answer is incorrect: count variable increases by 1         
            
        if self.count == 5: #produces new questions until 5 have been produced then moves to scoreboard screen
            Transition.end_transition(self) #calls function that moves user to scoreboard screen
            self.scoreboard = Label(self.scoreboard_screen, text = "You Scored {} out of 5".format(self.score), bg = BG, fg = FG, font = FT3, pady = PY2) #result statement on third screen
            self.scoreboard.grid(columnspan = 5, row = 2) #positioning result statement      
        else:
            self.next_question_geography() #call geography next question function
                     
            
    def check_answer_celebrities(self, Answer): #defining function which checks answer for celebrities questions
        if self.answer.get() == Answer: #checks users answer against correct answer set in above function
            self.score += 1 #if answer is correct: score variable increases by 1
            self.count += 1 #if answer is correct: count variable increases by 1       
        else:
            self.score += 0 #if answer is incorrect: score variable increases by 0
            self.count += 1 #if answer is incorrect: count variable increases by 1           
                
        if self.count == 5: #produces new questions until 5 have been produced then moves to scoreboard screen
            Transition.end_transition(self) #calls function that moves user to scoreboard screen
            self.scoreboard = Label(self.scoreboard_screen, text = "You Scored {} out of 5".format(self.score), bg = BG, fg = FG, font = FT3, pady = PY2) #result statement on third screen
            self.scoreboard.grid(columnspan = 5, row = 2) #positioning result statement      
        else:
            self.next_question_celebrities() #call celebrities next question function
                     
        
    def check_answer_dishes(self, Answer): #defining function which checks answer for national dishes questions
        if self.answer.get() == Answer: #checks users answer against correct answer set in above function
            self.score += 1 #if answer is correct: score variable increases by 1
            self.count += 1 #if answer is correct: count variable increases by 1 
        else:
            self.score += 0 #if answer is incorrect: score variable increases by 0
            self.count += 1 #if answer is incorrect: count variable increases by 1       
                
        if self.count == 5: #produces new questions until 5 have been produced then moves to scoreboard screen
            Transition.end_transition(self) #calls function that moves user to scoreboard screen  
            self.scoreboard = Label(self.scoreboard_screen, text = "You Scored {} out of 5".format(self.score), bg = BG, fg = FG, font = FT3, pady = PY2) #result statement on third screen
            self.scoreboard.grid(columnspan = 5, row = 2) #positioning result statement                     
        else:        
            self.next_question_dishes() #call national dishes next question function


if __name__ == "__main__": #main routine
    root = Tk()
    frames = Questions(root)
    root.title("General Knowledge Quiz")
    root.resizable(width = False, height = False)
    root.mainloop()