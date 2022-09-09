import math
num={'A':100,'B':80,'C':70,'D':60,'F':60}

person=input('Who are we calculating grades for? ')
# This line of code is asking for user input of whose grade is being calculated
print()
lab=int(input('Enter the Labs grade: '))
# THis line of code is asking for the Lab grade
print()
if lab > 100:
    lab=100
    print('lab score adjusted to 100')
elif lab < 0:
    lab = 0
    print('lab score adjusted to 0')
print()
# These are if,elif statements for the lab
exam=int(input('Enter the EXAMS grade: '))
print()
if exam > 100:
    print('Exam score adjusted to 100')
    exam= 100
elif exam < 0:
    print('Exam score adjusted to 0')
    exam = 0
print()
# These are if, eilf statements for exams
attendence=int(input('Enter the Attendence grade: '))
if attendence > 100:
    print('Attendence changed to 100')
    attendence = 100
elif attendence < 0:
    print('Attendence changed to 0')
    attendence = 0

#if,elif statements for attendence

print()
weight=float(lab*0.7+exam*0.2+attendence*0.1)

print('The weighted grade for',person,'is',weight)
if weight >= 90:
    print(person,'has a letter grade of A')
   
elif weight >= 80:
    print(person,'has a letter grade of B')
   
elif weight >= 70:
    print (person,'has a letter grade of C')

elif weight >= 60:
    print(person,'has a letter grade of D')
   
elif weight <= 60:
    print(person,'has a letter grade of F')
   

#if,elif statements for attendence

