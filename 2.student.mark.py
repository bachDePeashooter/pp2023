student = []
course = []
score = []
class Student:
    #declare
    def __init__(self, name:str, id:int, dob):
        self.name = name
        self.id = id
        self.dob = dob

    #print full student info
    def describe_student(self):
        print("-----")
        print(f'Name: {self.name.title()}\nID: {self.id}\nDay of birth: {self.dob}')
    
    #sth to print student name to add score
    def add_score_student(self):
        print("-----")
        mark = input(f'Enter score for {self.name.title()}: ')
        score.append(mark)

    #sth that print student name with student score
    def describe_score(self, i:int):
        print(f'{self.name.title()}: {score[i]}')

class Course:
    #declare
    def __init__(self, name:str):
        self.name = name

    #print course's name with a statement
    def describe_course(self, msg):
        print("-----")
        print(f'{msg} {self.name.title()}')

    #sth to print course name
    def add_score_course(self):
        print("-----")
        print(f'You are at {self.name.title()} course')

#Trapping users in infinite loop if they don't type anything
def ask_user(message=''):
    user_input = ''
    while not user_input:
        user_input = input(message)
    return user_input

#Fucntion to add student
def add_student():
    x = int(input('Enter the number of students you wanna add:'))
    for i in range(x):
        print("-----")
        name = ask_user("Enter Name: ")
        id = ask_user("Enter ID: ")
        dob = ask_user("Enter DOB: ")
        values = Student(name, id, dob)
        student.append(values)
    return student

#Fucntion to add course
def add_course():
    x = int(input('Enter the number of courses you wanna add:'))
    for i in range(x):
        print("-----")
        name = ask_user("Enter Name: ")
        values = Course(name)
        course.append(values)
    return course

#Add score for students
def add_score():
    if(len(student) == 0):
        print("you should find some student first")
        return add_student()
    elif(len(course) == 0):
        print("let's give them a course then else...")
        return add_course()
    else:
        for i in range(len(course)):
            course[i].add_score_course()
            for k in range(len(student)):
                student[k].add_score_student()

#Fucntion to print all student infos
def list_Of_Student():
    #in case someone forgot there is no student
    if(len(student) == 0):
        print("you should find some student first")
        return add_student()
    else:
        for a in range(len(student)):
            student[a].describe_student()

#Fucntion to print all course name
def list_Of_Course():
    #what if you have no courses?
    if(len(course) == 0):
        print("let's give them a course then... else")
        return add_course('Name: ')
    else: 
        for a in range(len(course)):
            course[a].describe_course('Name:')

def list_Of_Score():
    #Case that user forgot to add score
    if(len(score) == 0):
        print("did you finish their score yet, lazy")
        return add_score()
    
    #print option 
    for n in range(len(course)):
        course[n].describe_course(f'{n+1}.')

    #user input for a course
    ch = int(ask_user('Chose an option: '))

    #calculate starting point of the chosen course in score list
    i = len(student)*(ch-1)
    course[ch-1].describe_course('Here is the score for ')
    for count in range(len(student)):
        student[count].describe_score(i)
        i = i + 1

#Operating function
def Main_menu():
    print("---------------------")
    print("1.Add students \n2.Add course \n3.Print students list \n4.Print courses list \n5.Add marks for students \n6.Look at some mark \n7.Exit")
    print("---------------------")
    choice = str(input('Chose an action: '))
    match choice:
        case "1":
            add_student()
            return Main_menu()
        case "2":
            add_course()
            return Main_menu()
        case "3":
            list_Of_Student()
            return Main_menu()
        case "4":
            list_Of_Course()
            return Main_menu()
        case "5":
            add_score()
            return Main_menu()
        case "6":
            list_Of_Score()
            return Main_menu()
        case "7":
            print('GG')
        case _:
            print('Are you serious?')
            return Main_menu()

Main_menu()