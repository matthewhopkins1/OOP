#create an instance of student class and display age and when they can register

import StudentClass as sc

d = '1001'
n = 'John'
b = '10/11/2001'
c = 'Jr'

student1 = sc.Student(d, n, b, c)

student1.calc_age()
student1.calc_register()

print(f'Student age is: {student1.get_age()}')
print(f'Student can register between: {student1.get_register()}')