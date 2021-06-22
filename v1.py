from random import*

possible_question = []
current_question = ["a"]
text = open("questions.txt", "r")
for line in text.readlines():
    possible_question.append([line.split()[0], line.split()[1], line.split()[2],line.split()[3], line.split()[4]])
count = 0
while count <= 1:  
    current_question.clear()
    q = randrange(len(possible_question))
    for i in possible_question[q]:
        j = i.replace('-',' ')
        current_question.append(j)
    possible_question.pop(q)
    answer = current_question[1]
    if input("{}\nIs it {}, {}, {} or {}: ".format(current_question[0],current_question[1],current_question[2], current_question[3], current_question[4])) == answer:
        print("Correct!")
        count+=1
    else:
        print("Incorrect!")
        count+=1
    