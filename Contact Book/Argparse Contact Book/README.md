# Contact Book CLI

A simple command-line contact manager built with Python’s `argparse`.  
Manage your contacts directly from the terminal — add, edit, view, delete, or list them easily.

---

## 🚀 Features

- Add, edit, view, delete, and list contacts
- Data stored locally in `contacts.json`
- Optional colorized output using `colorama`
- Uses only Python standard libraries (with `colorama` as optional dependency)

---

## 🛠️ Installation

Clone the repository and navigate to the project directory:

```bash
"clone the repsistory and navigate to the project directory"
cd contact-book-cli
```

(Optional) Install `colorama` for colorized output:

```bash
pip install colorama
```

---

## 💻 Usage

Run the CLI tool using:

```bash
python contact_cli.py --help
```

### Add a Contact

```bash
python contact_cli.py add "Alice" --phone 12345 --email alice@mail.com --address "New York"
```

### Edit a Contact

```bash
python contact_cli.py edit "Alice" --phone 67890
```

### View a Contact

```bash
python contact_cli.py view "Alice"
```

### List All Contacts

```bash
python contact_cli.py list
```

### Delete a Contact

```bash
python contact_cli.py delete "Alice"
```

---

## 📂 Data Storage

All contacts are stored in a local JSON file:

```
contacts.json
```

Structure:

```json
{
  "Alice": {
    "phone": "12345",
    "email": "alice@mail.com",
    "address": "New York"
  }
}
```

---

## 🧩 Requirements

- Python 3.8+
- (Optional) `colorama` for colored terminal output

---

## 📜 License

This project is open-source and available under the MIT License.
