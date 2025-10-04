"""
Generates various types of passwords.

This module provides a framework for generating different kinds of passwords,
including PINs, random character passwords, and memorable passphrase-style
passwords.
"""

import random
import string
from abc import ABC, abstractmethod

import nltk


class PasswordGenerator(ABC):
    """An abstract base class for password generators."""

    @abstractmethod
    def generate(self):
        """Generates and returns a password."""
        pass


class PinGenerator(PasswordGenerator):
    """
    Generates a numeric PIN of a specified length.

    Args:
        length (int): The desired length of the PIN.
    """

    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        """
        Generates a random numeric PIN.

        Returns:
            str: The generated PIN.
        """
        return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """
    Generates a random password with options for numbers and symbols.

    Args:
        length (int): The desired length of the password. Defaults to 12.
        has_numbers (bool): Whether to include numbers. Defaults to False.
        has_symbols (bool): Whether to include symbols. Defaults to False.
    """

    def __init__(
        self, length: int = 12, has_numbers: bool = False, has_symbols: bool = False
    ):
        self.length = length
        self.characters = string.ascii_letters
        if has_numbers:
            self.characters += string.digits
        if has_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """
        Generates a random password from the allowed character set.

        Returns:
            str: The generated password.
        """
        return "".join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Generates a memorable password from a list of words.

    Args:
        num_words (int): The number of words to use. Defaults to 4.
        separator (str): The separator to use between words. Defaults to "-".
        capitalize (bool): Whether to randomly capitalize some words.
                           Defaults to False.
        vocabulary (list[str], optional): A list of words to use.
                                          If None, downloads and uses the NLTK
                                          English words corpus.
                                          Defaults to None.
    """

    def __init__(
        self,
        num_words: int = 4,
        separator: str = "-",
        capitalize: bool = False,
        vocabulary: list[str] | None = None,
    ):
        self.num_words = num_words
        self.separator = separator
        self.capitalize = capitalize

        if vocabulary:
            self.vocabulary = vocabulary
        else:
            try:
                nltk.data.find("corpora/words")
            except nltk.downloader.DownloadError:
                nltk.download("words", quiet=True)
            self.vocabulary = nltk.corpus.words.words()

    def generate(self) -> str:
        """
        Generates a memorable passphrase.

        Returns:
            str: The generated passphrase.
        """
        password_words = [
            random.choice(self.vocabulary) for _ in range(self.num_words)
        ]
        if self.capitalize:
            password_words = [
                word.upper() if random.choice([True, False]) else word.lower()
                for word in password_words
            ]
        return self.separator.join(password_words)


def main():
    """Generates and prints one of each type of password."""
    pin_password_generator = PinGenerator(8)
    print(f"Generated PIN: {pin_password_generator.generate()}")

    random_password_generator = RandomPasswordGenerator(
        length=16, has_numbers=True, has_symbols=True
    )
    print(f"Generated Random Password: {random_password_generator.generate()}")

    memorable_password_generator = MemorablePasswordGenerator(
        num_words=5, capitalize=True
    )
    print(f"Generated Memorable Password: {memorable_password_generator.generate()}")


if __name__ == "__main__":
    main()
