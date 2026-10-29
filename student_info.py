## The Lesson class represents all info about a class
#
from datetime import datetime
class Lesson :

   def __init__(self):

     self.name = input('Enter name of  the class?  ')

     self.time = input('What time is this class?  ')

     self.teacher_name = input("What is the teacher's name?  ")

 
   def info(self):
     print(f'  {self.name} in {self.time} by {self.teacher_name}')
     

## This Student class, is used to organize all information
## we might need/collect about a student during registration
#-----------------------------------------------------------
#
class Student:

     def __init__(self):
         self.firstname = input("Please enter the student's first name:  ")

         first_name = self.firstname

         print (f"IF YOU DON'T HAVE A MIDDLE NAME LEAVE THE NEXT QUESTION  BLANK")

         self.middlename = input (f'Please enter {first_name}\'s middle name: ')

         self.lastname= input (f'Please enter {first_name}\'s last name:')
         
         self.dob = input (f'what is {first_name}\'s  birth year? ' )

         self.age = datetime.now().year - int(self.dob)

         self.color = input (f'{first_name}\'s favorite color (optional): ')

         self.gender = input(f'what is {first_name}\'s  gender  ? ').upper()

         if self.gender.upper() == 'MALE':
             
             pronoun =('his')
     
         elif self.gender == 'FEMALE':
             
             pronoun =('her')    

         else:
             print('please print  male or female in the previous question')  

             exit(1)

         self.number_of_periods = int(input("How many periods? "))

         self.periods = []

         index = 1

         while index <= self.number_of_periods:

           period = Lesson()

           self.periods.append(period)

           index +=1

         self.favorite = int(input("Enter the number corresponding to your favorite period: "))

       

         while self.favorite > self.number_of_periods or self.favorite < 1:
             
             print("Invalid Input")
             self.favorite = int(input("Enter valid number corresponding to your favorite period: "))

        
         print(f'Nice, here is you favorite period:{self.favorite}')

         self.periods[self.favorite -1].info()

     def info(self):
        
    
        for x in self.periods:
             x.info()


## This is the actual program that does something
number_of_students = int(input("Please enter the number  of students you would like to register: "))
students = []
current_student = 1
while number_of_students > 0 :
    number_of_students = number_of_students - 1
    print(f'Enter info for student {current_student}')
    students.append(Student())
    current_student = current_student + 1

exit(0)
