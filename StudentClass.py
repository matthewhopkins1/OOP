from datetime import date

class Student:

    def __init__(self, d, n, b, c):
        self.__id = d
        self.__name = n
        self.__dob = b
        self.__classification = c
        self.__age = 0
        self.__register = 0

#create a method that will calculate students current age

    def age(self, b):
        self.__age = 

        
#create a method that will determine when student can register

    def register():
        if self.__classification == Sr:
            self.__register = '4/1 thru 4/3'
        elif self.__classification == Jr:
            self.__register = '4/4 thru 4/6'
        elif self.__classification == S:
            self.__register = '4/7 thru 4/9'
        else:
            self.__register = '4/10 thru 4/12'

#create a method to return age and another method to return registration dates

    def get_age(self):
        return self.__age

    def get_register(self):
        return self.__register