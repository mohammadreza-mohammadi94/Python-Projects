
# Contact Book Application

This is a simple command-line contact book application written in Python.

## Features

* Add new contacts
* Edit existing contacts
* View all contacts
* Delete contacts

## `ContactBook` Class

The `ContactBook` class is the main component of the application. It manages the contacts and provides methods to interact with them.

### `__init__(self)`

Initializes an empty contact book.

### `add_contact(self, name: str, phone: str, email: str, address: str)`

Adds a new contact to the contact book.

* **Parameters:**
    * `name` (str): The name of the contact.
    * `phone` (str): The phone number of the contact.
    * `email` (str): The email address of the contact.
    * `address` (str): The address of the contact.

### `view_contact(self)`

Displays all the contacts in the contact book.

### `delete_contact(self, name: str)`

Deletes a contact from the contact book.

* **Parameters:**
    * `name` (str): The name of the contact to delete.

### `edit_contact(self, name: str, phone: str = None, email: str = None, address: str = None)`

Edits an existing contact in the contact book.

* **Parameters:**
    * `name` (str): The name of the contact to edit.
    * `phone` (str, optional): The new phone number. Defaults to `None`.
    * `email` (str, optional): The new email address. Defaults to `None`.
    * `address` (str, optional): The new address. Defaults to `None`.

## How to Use

1. Run the `main.py` file from your terminal:

   ```bash
   python main.py
   ```

2. The application will display a menu with the following options:

   ```
   --- Contact Book Application ---
   1. Add contact
   2. Edit contact
   3. View contacts
   4. Delete contact
   5. Quit
   ```

3. Enter your choice and follow the prompts.
