# Nathan Hinebaugh
# CSC2017
# Project 4
# address_test

# imports the address class
import address_class


# defines the main function
def main():
    # declares the two addresses
    address1 = address_class.Address("1122", "North st.", "Colorado Springs",
                                     "CO", "80917", "102")
    address2 = address_class.Address("500", "NWest st.", "Colorado Springs",
                                     "CO", "8023", )
    # prints the two address to the screen
    print(address1)
    print(address2)

    # compares the two addresses using the come before function in the class file.
    address1.comes_before(address2)


if __name__ == "__main__":
    main()
