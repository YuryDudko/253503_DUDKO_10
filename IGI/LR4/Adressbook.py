# AddressBook class for managing contacts and saving/loading them to/from files
import csv
import pickle
from Contact import *

class AddressBook:
    def __init__(self):
        """
        Initialize an AddressBook object with an empty list of contacts.
        """
        self.contacts = []

    def __str__(self):
        return self.text


    def add_contact(self, contact):
        """
        Add a contact to the address book.

        Args:
            contact (Contact): Contact object to add.
        """
        self.contacts.append(contact)

    def save_to_csv(self, filename):
        """
        Save contacts to a CSV file.

        Args:
            filename (str): Name of the CSV file.
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.serialize())

    def save_to_pickle(self, filename):
        """
        Save contacts to a pickle file.

        Args:
            filename (str): Name of the pickle file.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    @staticmethod
    def load_from_csv(filename):
        """
        Load contacts from a CSV file.

        Args:
            filename (str): Name of the CSV file.

        Returns:
            AddressBook: AddressBook object with loaded contacts.
        """
        address_book = AddressBook()
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                address_book.add_contact(Contact.deserialize(row))
        return address_book

    @staticmethod
    def load_from_pickle(filename):
        """
        Load contacts from a pickle file.

        Args:
            filename (str): Name of the pickle file.

        Returns:
            AddressBook: AddressBook object with loaded contacts.
        """
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
        address_book = AddressBook()
        address_book.contacts = contacts
        return address_book

    def find_contact_by_surname(self, surname):
        """
        Find a contact by surname in the address book.

        Args:
            surname (str): Surname of the contact to find.

        Returns:
            Contact or None: Contact object if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.surname.lower() == surname.lower():
                return contact
        return None

    def find_contact_by_phone(self, phone):
        """
        Find a contact by phone number in the address book.

        Args:
            phone (str): Phone number of the contact to find.

        Returns:
            Contact or None: Contact object if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
        return None
