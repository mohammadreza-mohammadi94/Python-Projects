# Contact Book

Small, educational Contact Book project with two CLI options:

- Legacy interactive CLI: `CLI-Based Contact Book/main.py` — a simple menu-driven in-memory contact book (no persistence).
- Argparse-based CLI: `Argparse Contact Book/contact_cli.py` — modern command-line tool with JSON persistence and optional colored output.

Features

- Add, edit, view, list and delete contacts
- JSON persistence (file: `src/contacts.json`) for the argparse CLI
- Optional colorized output using `colorama`

Quick start

1. (Optional) Create a virtual environment and activate it:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install optional dependencies (color output):

```powershell
pip install -r requirements.txt
```

Argparse CLI usage

Run the modern CLI at `src/Argparse Contact Book/contact_cli.py`.

Examples:

```powershell
# Add a contact
python "src/Argparse Contact Book/contact_cli.py" add "Alice" --phone "555-1234" --email "alice@example.com" --address "123 Lane"

# List contacts
python "src/Argparse Contact Book/contact_cli.py" list

# View a specific contact
python "src/Argparse Contact Book/contact_cli.py" view "Alice"

# Edit a contact (only provide fields to change)
python "src/Argparse Contact Book/contact_cli.py" edit "Alice" --phone "555-0000"

# Delete a contact
python "src/Argparse Contact Book/contact_cli.py" delete "Alice"
```

Notes

- If `colorama` is not installed the CLI will run without colored text.
- Contacts are stored in `src/contacts.json` for the argparse CLI. Keep backups if you edit it manually.
- The legacy interactive CLI (`src/CLI-Based Contact Book/main.py`) stores contacts only in memory and will lose data when the program exits.

Contributing

- Add unit tests under a `tests/` folder
- Implement import/export (CSV/vCard)
- Add more robust validation for phone/email fields

License

This is a simple educational project — add a license file if you intend to share it publicly.
