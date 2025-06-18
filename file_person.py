# Nathan Hinebaugh
# CSC2017
# Project 3
# File person

# define the class
class Person:
    # defines the initializer with all variables needed for program
    def __init__(self, first_name, middle_initial, last_name, date_of_birth, ):
        self.__first_name = first_name
        self.__middle_initial = middle_initial
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth

    # set and get statement for first name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    # set and get statement for middle initial
    def get_middle_initial(self):
        return self.__middle_initial

    def set_middle_initial(self, middle_initial):
        self.__middle_initial = middle_initial

    # get and set statement for last name
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    # get and set statement for date of birth
    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    # defining string for output of full name and DOB.
    def __str__(self):
        full_name = f"Full Name: {self.__first_name} {self.__middle_initial} {self.__last_name}" + \
                    f"\n\tDate of birth: {self.__date_of_birth}"

        return full_name
