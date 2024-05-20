# Contact class for managing individual contacts
class Contact:
    def __init__(self, name, phone):
        """
        Initialize a Contact object with name and phone number.

        Args:
            name (str): Name of the contact.
            phone (str): Phone number of the contact.
        """
        self.name = name
        self.phone = phone

    def __str__(self):
        """
        Return a string representation of the contact.

        Returns:
            str: String representation of the contact.
        """
        return f"{self.name}: {self.phone}"

    def serialize(self):
        """
        Serialize the contact object into a dictionary.

        Returns:
            dict: Serialized form of the contact object.
        """
        return {"name": self.name, "phone": self.phone}

    @staticmethod
    def deserialize(data):
        """
        Deserialize a dictionary into a Contact object.

        Args:
            data (dict): Serialized form of the contact.

        Returns:
            Contact: Deserialized contact object.
        """
        return Contact(data["name"], data["phone"])
