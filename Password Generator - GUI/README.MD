# Password Generator - GUI

This small Python project provides a set of password generators and a minimal GUI wrapper. It includes utilities to create numeric PINs, random-character passwords (with options for numbers and symbols), and memorable passphrase-style passwords built from an English word list.

The code in this project is located under `src/`. The key module is `password_generators.py` which defines three generator classes:

- `PinCodeGenerator` — produce numeric PINs of a requested length.
- `RandomPasswordGenerator` — produce random-character passwords with optional digits and symbols.
- `MemorablePasswordGenerator` — build passphrases by joining words from an English vocabulary (optionally capitalizing words).

Files of interest
- `src/password_generators.py` — implementations for the generators and a simple `main()` used for quick CLI testing.
- `src/app.py` — (GUI entry point) wires the generators into a user interface (see the file for details).

Requirements

- Python 3.8+ is recommended.
- The project optionally uses the NLTK word corpus for the memorable passphrase generator. If NLTK is not available or the corpus is not installed the code will attempt to download the `words` corpus at runtime.

Quick setup

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if you use the provided `requirements.txt`):

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt` in this directory, you likely only need `nltk` (and any GUI framework used by `src/app.py` — e.g. `tkinter` is included with many Python installs; `streamlit` or `PySimpleGUI` would be installed separately if used):

```powershell
pip install nltk
```

NLTK corpus (if needed)

When using `MemorablePasswordGenerator` without providing a custom vocabulary, the code attempts to ensure the NLTK `words` corpus is available. If the corpus isn't present it will attempt to download it automatically. To pre-install the corpus manually (recommended for offline or controlled setups), run a Python shell and do:

```python
import nltk
nltk.download('words')
```

Usage

- Run a quick command-line test of the generators:

```powershell
python src/password_generators.py
```

- Launch the GUI (if `src/app.py` is the GUI entry point; check the file contents to confirm which GUI framework is used):

```powershell
python src/app.py
```

Notes and tips

- The memorable passphrase generator uses the full NLTK words corpus; some words in the corpus are uncommon or archaic. If you prefer a curated wordlist, pass a custom `vocabulary` list into `MemorablePasswordGenerator`.
- The random password generator uses `string.punctuation` for symbols which may include shell-sensitive characters. If you plan to paste passwords into shells, consider using the `has_symbols=False` option or sanitizing the output.
- The code is intentionally small and easy to extend. Adding a new generator class is straightforward — subclass `PasswordGenerator` and implement `generate()`.

License

This repository contains small utility code intended for learning and personal use. Update the license section if you want to publish this code (for example, add an `MIT` or other license file).

Contributing

If you'd like help improving the GUI or adding features (for example: copy-to-clipboard buttons, strength meters, or curated wordlists), open an issue or send a pull request with tests.

Contact

Drop a message in the repo or reach out to the project owner for questions.
