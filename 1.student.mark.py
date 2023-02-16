student = []
courses = []
marks = []

def mkstudent():
    print('Enter the number of student in class:')
    x = input()
    print('There are ' + x + ' in class')
    for i in range(int(x)):
        print('Enter the info of student ' + str(i+1))
        print('Name: ')
        name = input()
        student.append(name)
        print('ID: ')
        id = input()
        student.append(id)
        print('DoB: ')
        dob = input()
        student.append(dob)


def mkcourse():
    print('Enter the number of courses:')
    x = input()
    print('There are ' + x +' courses')
    for i in range(int(x)):
        print('Enter the info of course number ' + str(i+1))
        print('Name: ')
        name = input()
        courses.append(name)
        print('ID: ')
        id = input()
        courses.append(id)

def liststudent():
    print('--------------------------------')
    print('Name' + '  ' + 'Student ID' + '  ' + 'DoB')
    for i in range(0,len(student),3):
        print(student[i] + '  ' + student[i+1] + '        ' + student[i+2])

def listcourse():
    print('--------------------------------')
    print('Course ID' + '  ' + 'Course name')
    for f in range(0,len(courses),2):
        print(courses[f] + '         ' + courses[f+1])

def slcourse():
    print('--------------------------------')
    for p in range(0,len(courses),2):
        p = int(p)
        print(str(int(p/2+1)) + '  ' + courses[p])

    print('Chose a course to continue: ')
    choice = input()
    choice = int(choice)
    print('You have chose  ' + courses[choice-1])

    print('--------------------------------')
    print('Name' + '  ' + 'Student ID' + '  ' + 'Mark')
    s = (choice-1)*(len(student)//3)
    y = 0
    for t in range(s,len(student),1):
        print(student[y] + '     ' + student[y+1] + '         ' + marks[t])
        y = y + 3


def ismark():
    for n in range(0,len(courses),2):
        print("Enter mark of " + courses[n])
        for m in range(0,len(student),3):
            print(student[m] + ' : ')
            score = input()
            marks.append(score)

mkstudent()
mkcourse()
ismark()
slcourse()
            



