# Task 1: Program to manage an address book and save contacts to files
# Lab Assignment: #4
# Version: 1.0
# Developer: Yury Dudko
# Date: 20.04.2024

from Adressbook import *
from Contact import Contact
from decorator import *

@repeat_execution
def task_1():
    # Create an address book
    address_book = AddressBook()

    # Add contacts to the address book
    address_book.add_contact(Contact("John Doe", "123456789"))
    address_book.add_contact(Contact("Jane Smith", "987654321"))

    # Save contacts to CSV and pickle files
    address_book.save_to_csv("contacts.csv")
    address_book.save_to_pickle("contacts.pickle")

    # Load contacts from CSV and pickle files
    loaded_address_book_csv = AddressBook.load_from_csv("contacts.csv")
    loaded_address_book_pickle = AddressBook.load_from_pickle("contacts.pickle")

    # Display contacts loaded from CSV
    print("Contacts from CSV:")
    for contact in loaded_address_book_csv.contacts:
        print(contact)

    # Display contacts loaded from pickle
    print("\nContacts from pickle:")
    for contact in loaded_address_book_pickle.contacts:
        print(contact)

    # Find contact by surname
    surname_to_find = input("Enter surname to find in the address book: ")
    found_contact_by_surname = address_book.find_contact_by_surname(surname_to_find)
    if found_contact_by_surname:
        print(f"Contact found by surname '{surname_to_find}': {found_contact_by_surname}")
    else:
        print(f"No contact found with surname '{surname_to_find}'")

    # Find contact by phone number
    phone_to_find = input("Enter phone number to find in the address book: ")
    found_contact_by_phone = address_book.find_contact_by_phone(phone_to_find)
    if found_contact_by_phone:
        print(f"Contact found by phone '{phone_to_find}': {found_contact_by_phone}")
    else:
        print(f"No contact found with phone '{phone_to_find}'")

# def main():
#     test_address_book()


# if __name__ == "__main__":
#     main()