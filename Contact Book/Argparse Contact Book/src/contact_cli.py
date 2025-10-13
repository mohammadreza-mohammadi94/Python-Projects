"""Contact Book CLI using argparse.

Features:
- Subcommands: add, edit, view, delete, list
- Optional color output using `colorama` (falls back to plain text)
- Simple JSON persistence file (`contacts.json`) in the same directory

This file depends only on Python standard library, with optional
colorama for colorized output. To install colorama:

    pip install colorama

Run `python contact_cli.py --help` for usage information.
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Dict

try:
    from colorama import Fore, Style, init as colorama_init

    colorama_init(autoreset=True)
    COLORS_AVAILABLE = True
except Exception:
    # colorama is optional; if not present we'll print plain text
    COLORS_AVAILABLE = False
    # Provide no-op placeholders so references to Fore/Style don't fail.
    class _NoColor:
        RED = ""
        GREEN = ""
        YELLOW = ""
        CYAN = ""

    Fore = _NoColor()
    class _NoStyle:
        RESET_ALL = ""

    Style = _NoStyle()


STORAGE_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def colored(text: str, color: str) -> str:
    if not COLORS_AVAILABLE:
        return text
    return f"{color}{text}{Style.RESET_ALL}"


class ContactBookStorage:
    """Tiny JSON-backed storage for contacts.

    The storage structure mirrors the in-memory `ContactBook` used in
    the example: a mapping of name -> {phone, email, address}.
    """

    def __init__(self, path: str = STORAGE_FILE):
        self.path = path
        self._data: Dict[str, Dict[str, str]] = {}
        self._load()

    def _load(self) -> None:
        if not os.path.exists(self.path):
            self._data = {}
            return
        try:
            with open(self.path, "r", encoding="utf-8") as fh:
                self._data = json.load(fh)
        except Exception:
            # If the file is corrupted, reset to empty to avoid crashes.
            self._data = {}

    def _save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self._data, fh, indent=2, ensure_ascii=False)

    def add(self, name: str, phone: str, email: str, address: str) -> None:
        if name in self._data:
            raise ValueError("Contact already exists")
        self._data[name] = {"phone": phone, "email": email, "address": address}
        self._save()

    def edit(self, name: str, phone: str | None, email: str | None, address: str | None) -> None:
        if name not in self._data:
            raise ValueError("Contact not found")
        if phone:
            self._data[name]["phone"] = phone
        if email:
            self._data[name]["email"] = email
        if address:
            self._data[name]["address"] = address
        self._save()

    def delete(self, name: str) -> None:
        if name not in self._data:
            raise ValueError("Contact not found")
        del self._data[name]
        self._save()

    def list_all(self) -> Dict[str, Dict[str, str]]:
        return dict(self._data)

    def get(self, name: str) -> Dict[str, str] | None:
        return self._data.get(name)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Contact Book CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Add a new contact")
    p_add.add_argument("name")
    p_add.add_argument("--phone", required=True)
    p_add.add_argument("--email", required=True)
    p_add.add_argument("--address", required=True)

    # edit
    p_edit = sub.add_parser("edit", help="Edit an existing contact")
    p_edit.add_argument("name")
    p_edit.add_argument("--phone")
    p_edit.add_argument("--email")
    p_edit.add_argument("--address")

    # view
    p_view = sub.add_parser("view", help="View a contact by name")
    p_view.add_argument("name")

    # list
    sub.add_parser("list", help="List all contacts")

    # delete
    p_delete = sub.add_parser("delete", help="Delete a contact")
    p_delete.add_argument("name")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = make_parser()
    args = parser.parse_args(argv)

    storage = ContactBookStorage()

    try:
        if args.command == "add":
            storage.add(args.name, args.phone, args.email, args.address)
            print(colored("Contact added", Fore.GREEN) if COLORS_AVAILABLE else "Contact added")

        elif args.command == "edit":
            storage.edit(args.name, args.phone, args.email, args.address)
            print(colored("Contact updated", Fore.YELLOW) if COLORS_AVAILABLE else "Contact updated")

        elif args.command == "view":
            contact = storage.get(args.name)
            if not contact:
                raise ValueError("Contact not found")
            print(colored(args.name, Fore.CYAN) if COLORS_AVAILABLE else args.name)
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}")

        elif args.command == "list":
            data = storage.list_all()
            if not data:
                print("No contacts found")
                return
            for name, info in data.items():
                name_str = colored(name, Fore.CYAN) if COLORS_AVAILABLE else name
                print(f"{name_str}: {info['phone']} | {info['email']} | {info['address']}")

        elif args.command == "delete":
            storage.delete(args.name)
            print(colored("Contact deleted", Fore.RED) if COLORS_AVAILABLE else "Contact deleted")

    except ValueError as exc:
        print(colored(f"Error: {exc}", Fore.RED) if COLORS_AVAILABLE else f"Error: {exc}")


if __name__ == "__main__":
    main()
