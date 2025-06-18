# Nathan Hinebaugh
# CSC2017
# Project 3
# personTest

# imports Date time and code file
import datetime
import file_person


# defines the main function
def main():
    # defines the people and their information
    person_1 = file_person.Person("Bob", "J", "Anderson", datetime.date(2000, 6, 25))
    person_2 = file_person.Person("Thor", "L", "Odinson", datetime.date(1000, 1, 1))
    person_3 = file_person.Person("Loki", "K", "Odinson", datetime.date(1000, 1, 2))
    person_4 = file_person.Person("Jane", "S", "Fonda", datetime.date(1937, 12, 21))
    person_5 = file_person.Person("Ryan", "R", "Reynolds", datetime.date(1976, 10, 23))
    # print statements for each person
    print(person_1)
    print(person_2)
    print(person_3)
    print(person_4)
    print(person_5)


# activating the main function
if __name__ == "__main__":
    main()
