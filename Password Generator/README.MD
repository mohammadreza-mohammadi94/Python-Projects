# Password Generator

This project is a Python script for generating various types of passwords. It provides a flexible framework for creating PINs, complex random passwords, and memorable passphrases.

## Features

- **PIN Generation**: Create simple numeric PINs of any length.
- **Random Password Generation**: Generate strong, random passwords including a mix of uppercase letters, lowercase letters, numbers, and symbols.
- **Memorable Passphrase Generation**: Create secure, easy-to-remember passphrases by joining words from a dictionary.

## Requirements

- Python 3.x
- `nltk`

## Installation

1.  **Clone the repository or download the source code.**

2.  **Navigate to the project directory:**
    ```bash
    cd "<your-path-to-project-directory>"
    ```

3.  **Install the required dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```
    The first time you run the script, `nltk` will download the necessary `words` corpus.

## Usage

To run the script and generate one of each type of password, execute the `main.py` file:

```bash
python src/main.py
```

### Example Output

The script will print a new set of generated passwords each time it is run. The output will look similar to this:

```
Generated PIN: 83061942
Generated Random Password: K&v9@*p$L#2!sW7a
Generated Memorable Password: unken-UNFRIENDLY-unowing-TOCSIN-subidar
```

## Code Overview

The script uses an object-oriented approach with an abstract base class `PasswordGenerator` that defines the common interface for all generators.

- **`PinGenerator`**: A simple class that generates a numeric string of a specified length.
- **`RandomPasswordGenerator`**: Generates a password from a character set that can include letters, numbers, and symbols based on the arguments provided.
- **`MemorablePasswordGenerator`**: Generates a passphrase by selecting random words from the NLTK English dictionary and joining them with a separator. It also supports random capitalization.
