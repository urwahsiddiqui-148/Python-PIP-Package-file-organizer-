# Python-PIP-Package-file-organizer-
Smart File Organizer is a Python-based command-line tool that helps you automatically organize files into categories like Documents, Images, Audio, and Videos. It can also detect and move duplicate files into a separate folder for easy cleanup.
Perfect 👍 Here’s the full README.md in one single block for your project, ready to use:

# 📂 Smart File Organizer  

**Smart File Organizer** is a Python-based command-line tool that helps you automatically organize files into categories like **Documents, Images, Audio, and Videos**. It can also **detect and move duplicate files** into a separate folder for easy cleanup.  

---

## 🚀 Installation  

You can install the package directly from **PyPI**:  

```bash
pip install urwah-smart-file-organizer


Or clone the repository and install locally:

git clone https://github.com/your-username/smart-file-organizer.git
cd smart-file-organizer
pip install -e.
```

## ⚡ Usage

Run the organizer using the CLI:

```bash
python -m smart_file_organizer.cli --path ./your_folder --check-duplicates

Options:

--path → Path to the folder you want to organize.

--check-duplicates → Moves duplicate files into a Duplicates/ folder.

--ml-similarity → Uses perceptual image hashing for duplicate image detection.

--log-path → Custom path to save logs (default: input folder).

--dry-run → Preview actions without moving files.

```

## 📁 Example

Suppose you have a folder sample_test with mixed files:

```bash

python -m smart_file_organizer.cli --path ./sample_test --check-duplicates

```


After running the command:

An organized/ folder will be created with subfolders:

Documents/ (pdf, docx, txt, etc.)

Images/ (jpg, png, gif, etc.)

Audio/ (mp3, wav, etc.)

Videos/ (mp4, mkv, avi, etc.)

A Duplicates/ folder will also be created (if duplicates are found).

A log report (smart_file_organizer_report.csv) will be generated in the given path.

## 🛠 Features

✅ Automatically organizes files by type

✅ Detects and separates duplicate files

✅ Supports perceptual image hashing (ML-based similarity detection)

✅ Generates a CSV log report of all actions

✅ Easy-to-use CLI tool

✅ Lightweight and fast

## 🤝 Contributing

Contributions are welcome!

Fork the repo

Create your feature branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add feature')

Push to branch (git push origin feature-name)

Open a Pull Request

## 📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.


