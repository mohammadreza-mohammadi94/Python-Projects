"""Simple Contact Book CLI module.

This module provides a minimal in-memory contact book implementation
intended for learning and small scripts. Contacts are stored in a
dictionary keyed by contact name. Each contact stores phone, email and
address fields.

Notes:
- Data is not persisted to disk. For persistence, serialize the
  `contacts` dictionary to JSON or use a lightweight database.
- Names are used as unique identifiers; adding two contacts with the
  same name will raise a ValueError.
"""


class ContactBook:
    """Manage a small collection of contacts in memory.

    Attributes
    ----------
    contacts : dict
        Mapping of contact name -> info dict with keys 'phone', 'email',
        and 'address'. Example:

        {
            'Alice': {'phone': '555-1234', 'email': 'alice@example.com', 'address': '...'},
        }
    """

    def __init__(self):
        # Initialize an empty contact dictionary
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email: str, address: str) -> None:
        """Add a new contact.

        Parameters
        ----------
        name : str
            Unique name of the contact (used as lookup key).
        phone : str
            Phone number string.
        email : str
            Email address string.
        address : str
            Postal or street address string.

        Raises
        ------
        ValueError
            If a contact with the same name already exists.
        """
        if name in self.contacts:
            raise ValueError("Contact already exists.")

        # Store contact information as a simple dict
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address,
        }
        print("Contact added successfully!")

    def view_contact(self) -> None:
        """Print all contacts to stdout.

        The method iterates over stored contacts and prints a single-line
        summary for each. For larger datasets you would return the data
        structure instead of printing, or implement pagination.
        """
        for name, info in self.contacts.items():
            print(
                f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}"
            )

    def delete_contact(self, name: str) -> None:
        """Delete a contact by name.

        Parameters
        ----------
        name : str
            The name of the contact to delete.

        Raises
        ------
        ValueError
            If the contact does not exist.
        """
        if name not in self.contacts:
            raise ValueError("Contact does not exist.")

        del self.contacts[name]

    def edit_contact(
        self, name: str, phone: str | None = None, email: str | None = None, address: str | None = None
    ) -> None:
        """Edit fields of an existing contact.

        Only non-None arguments are applied; passing `None` leaves the
        existing value unchanged.
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print("Contact updated successfully!")
            return
        # If the contact isn't found, inform the caller (no exception
        # here to keep the CLI experience simple).
        print("Contact not found")


if __name__ == "__main__":
    # Simple interactive command-line interface for the ContactBook.
    # This keeps the example self-contained and easy to run during
    # development or learning. For larger projects the CLI would be put
    # behind a separate runner or command parser (argparse / click).
    book = ContactBook()

    while True:
        print("\n--- Contact Book Application ---")
        print("1. Add contact")
        print("2. Edit contact")
        print("3. View contacts")
        print("4. Delete contact")
        print("5. Quit")
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            # Collect fields and add a contact
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            try:
                book.add_contact(name, phone, email, address)
            except ValueError as exc:
                print(f"Error adding contact: {exc}")

        elif user_choice == '2':
            # Edit an existing contact; blank inputs are treated as
            # "leave unchanged" by converting empty strings to None.
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.edit_contact(name, phone or None, email or None, address or None)

        elif user_choice == '3':
            print("\nList of Contacts:")
            book.view_contact()

        elif user_choice == '4':
            name = input("\nEnter name of contact to delete: ")
            try:
                book.delete_contact(name)
                print("Contact deleted successfully!")
            except ValueError as exc:
                print(f"Error deleting contact: {exc}")

        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")