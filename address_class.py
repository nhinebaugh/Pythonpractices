# Nathan Hinebaugh
# CSC2017
# Project 4
# address_class


class Address:
    # defines the initializer with all variables needed for program
    def __init__(self, house_number, street, city, state, postal_code, apt_numb=""):
        self.__house_number = house_number
        self.__street = street
        self.__apt_numb = apt_numb
        self.__city = city
        self.__state = state
        self.__postal_code = postal_code

    # set and get statement for house number
    def get_house_number(self):
        return self.__house_number

    def set_house_number(self, house_number):
        self.__house_number = house_number

    # set and get statement for street name
    def get_street(self):
        return self.__street

    def set_street(self, street):
        self.__street = street

    # get and set statement for optional apartment number
    def get_apt_numb(self):
        return self.__apt_numb

    def set_apt_numb(self, apt_numb):
        self.__apt_numb = apt_numb

    # get and set statement for city
    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    # get and set statement for state
    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    # get and set statement for postal code
    def get_postal_code(self):
        return self.__postal_code

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    # defines the function that compares the two addresses. 
    def comes_before(self, another_address):
        if self.get_postal_code() > another_address.get_postal_code():
            print(f"The first address comes before the second one.")
            return 1

        elif self.get_postal_code() < another_address.get_postal_code():
            print(f"The second address comes before the first.")
            return -1

        else:
            print(f"Addresses are the same.")
            return 0

    # defining string for output of full address on two lines
    def __str__(self):
        address = f"Address: {self.__house_number} {self.__street} Apt. {self.__apt_numb}" + \
                  f"\n{self.__city} {self.__state} {self.__postal_code}"

        return address
