student = []
courses = []
marks = []
#add student
def mkstudent():
    x = input('Enter the number of student in class:')
    print('There are ' + x + ' in class')
    for i in range(int(x)):
        print('Enter the info of student ' + str(i+1))
        name = input('Name: ')
        student.append(name)
        id = input('ID: ')
        student.append(id)
        dob = input('DoB: ')
        student.append(dob)

#add course
def mkcourse():
    x = input('Enter the number of courses:')
    print('There are ' + x +' courses')
    for i in range(int(x)):
        print('Enter the info of the course number ' + str(i+1))
        name = input('Name: ')
        courses.append(name)
        id = input('ID: ')
        courses.append(id)

#add marks for students
def insertmark():
    if(len(courses) == 0):
        print("insert a fukin course")
        return mkcourse()
    for n in range(0,len(courses),2):
        print("Enter mark of " + courses[n])
        for m in range(0,len(student),3):
            print(student[m] + ' : ')
            score = input()
            marks.append(score)

#print student
def liststudent():
    sth_went_wrong()
    print('--------------------------------')
    print('Name' + '  ' + 'Student ID' + '  ' + 'DoB')
    for i in range(0,len(student),3):
        print(student[i] + '  ' + student[i+1] + '        ' + student[i+2])

#print course
def listcourse():
    sth_went_wrong()
    print('--------------------------------')
    print('Course ID' + '  ' + 'Course name')
    for f in range(0,len(courses),2):
        print(courses[f] + '         ' + courses[f+1])

#print mark for selected course
def selectcourse():
    sth_went_wrong()
    print('--------------------------------')
    for p in range(0,len(courses),2):
        p = int(p)
        print(str(int(p/2+1)) + '  ' + courses[p])

    choice = input('Chose a course to continue: ')
    choice = int(choice)
    print('You have chose  ' + courses[choice-1])
    ch = (choice-1)*len(student)//3

    print('--------------------------------')
    print('Name' + '  ' + 'Student ID' + '  ' + 'Mark')
    for i in range(0,len(student),3):
        print(student[i] + '  ' + student[i+1] + '        ' + marks[ch])
        ch = ch + 1

#case that someone FORGET add or mean to wrong
def sth_went_wrong():
    if(len(courses) == 0):
        print("insert a fukin course")
        return mkcourse()
    if(len(student) == 0):
        print("insert a fukin student")
        return mkstudent()
    if(len(marks) == 0):
        print("insert a fukin mark")
        return insertmark()

#main menu
def management():
    print("\n\n1.Add students \n2.Add course \n3.Print students list \n4.Print courses list \n5.Add marks for students \n6.Look at some mark \n7.exit")
    lang = str(input("Chose an option or leave da fug out a here: "))
    match lang:
        case "1":
            mkstudent()
            return management()
        
        case "2":
            mkcourse()
            return management()
            
        case "3":
            liststudent()
            return management()
            
        case "4":
            listcourse()
            return management()
            
        case "5":
            insertmark()
            return management()

        case "6":
            selectcourse()
            return management()
        
        case "7":
            print("Bye")
            
        
        case _:
            print("u should exit to learn some number\n")
            return management()

management()
    

