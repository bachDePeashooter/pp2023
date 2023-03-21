import datetime
import math
import numpy as np

student = []
course = []

class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def getStudent(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getDoB(self):
        return self.dob
    
    def addStudent():
        x = askForInt('Number of students: ')
        for i in range(x):
            name = input("Enter Name: ")
            id = askForDistinct("Enter ID: ")
            dob = askForDoB('Enter Day of Birth (dd/mm/yyyy): ')
            values = Student(name, id, dob)
            student.append(values)

    def displayStudent(self):
        print("-----")
        print(f'Name: {self.name.title()}\nID: {self.id}\nDay of birth: {self.dob}')
    
class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
    
    def getCourse(self):
        return self.name
    
    def getCredit(self):
        return self.credits
    
    def addCourse():
        x = askForInt('Number of courses: ')
        for i in range(x):
            name = input("Enter Name: ")
            credits = askForInt("Enter credits: ")
            value = Course(name, credits)
            course.append(value)

    
    def displayCourse(self):
        print("-----")
        print(f'Course: {self.name.title()}\n Credits: {self.credits} ETCS')

    
def askForInt(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("A number plsssss")
            continue
        if value < 0:
            print("And it should be positive")
            continue
        else:
            break
    return value

def askForDistinct(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("A number plsssss")
            continue
        if value < 0:
            print("And it should be positive")
            continue
        for i in range(len(student)):
            a = Student.getId(student[i])
            if a == value:
                print('sowwie it already exist')
                break
        else:
            break
    return value

def askForDoB(prompt):
    while True :
        DOB = input(prompt)
        try :
            DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
            break
        except ValueError:
            print("Error: must be format dd/mm/yyyy ")
            continue
    return DOB


mark = []
def addMark():
    if len(student) == 0:
        print('Where are the students? ')
        return Student.addStudent()
    if len(course) == 0:
        print('You must teach them something, right?')
        return Course.addCourse()
    else:
        for i in range(len(course)):
            markInEachCourse = []
            for j in range(len(student)):
                score = askForInt(f'Enter {Course.getCourse(course[i])} mark for {Student.getStudent(student[j])}: ')
                markInEachCourse.append(score)
            mark.append(markInEachCourse)

def getMark():
    AllMark = np.array(mark)

    for n in range(len(course)):
        print(f'{n+1}. {Course.getCourse(course[n]).title()}')
    
    ch = 100 #just initialize variable 'ch' as integer which should be bigger than len(Course)
    while ch > len(course):
        ch = askForInt('Enter your choice: ')
    
    ch = ch - 1
    print("-----")
    print(f'Here is the mark of {Course.getCourse(course[ch]).title()}')
    for i in range(len(student)):
        print(f'{Student.getStudent(student[i]).title()}: {AllMark[ch,i]}')

def getGPA():
    AllMark = np.array(mark)
    GPA = []
    totalCredit = 0
    for i in range(len(course)):
        totalCredit += Course.getCredit(course[i])
        
    for i in range(len(student)):
        sumMark = 0
        for j in range(len(course)):
            sumMark = AllMark[j,i] * Course.getCredit(course[j]) + sumMark
        val = math.floor(sumMark/totalCredit)
        GPA.append(val)
    
    GPA = np.array_split(GPA, len(student))
    GPA = np.array(GPA)

    #sorting student
    #make a list of student name
    name = []
    for i in range(len(student)):
        name.append(Student.getStudent(student[i]).title())
    name = np.array_split(name, len(student))

    #merge student name with GPA 
    ascendingRank = np.concatenate((name,GPA),axis = 1)

    #sorting GPA column
    ascendingRank = sorted(ascendingRank, key=lambda a_entry: a_entry[1])

    #change type of array
    ascendingRank = np.array(ascendingRank)

    #reverse the matrix to descending order
    descendingRank = ascendingRank[::-1]

    print('bachDePeashooter server ranking')
    for i in range(len(student)):
        print(f'{i+1}. {descendingRank[i,0]}: {descendingRank[i,1]}')
        
    
        

def Main_menu():
    print("---------------------")
    print("1.Add students \n2.Add course \n3.Print students list \n4.Print courses list \n5.Add marks for students \n6.Print all mark of a course\n7.Top server ranking \n8.Exit")
    print("---------------------")
    choice = str(input('Chose an action: '))
    match choice:
        case "1":
            Student.addStudent()
            return Main_menu()
        case "2":
            Course.addCourse()
            return Main_menu()
        case "3":
            if len(student) == 0:
                print('Let adopt some student')
                Student.addStudent()
                return Main_menu()
            else:
                for i in range(len(student)):
                    Student.displayStudent(student[i])
                return Main_menu()
        case "4":
            if len(course) == 0:
                print('Give em something to learrrn')
                Course.addCourse()
                return Main_menu()
            else:
                for i in range(len(course)):
                    Course.displayCourse(course[i])
                return Main_menu()
        case "5":
            addMark()
            return Main_menu()
        case "6":
            if len(mark) == 0:
                return addMark()
            else:
                getMark()
                return Main_menu()
        case "7":
            if len(mark) == 0:
                return addMark()
            else:
                getGPA()
                return Main_menu()
        case "8":
            print('GG')
        case _:
            print('Are you serious?')
            return Main_menu()

Main_menu()
