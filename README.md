# 🔐 File Integrity Monitor

This is a simple Python tool that monitors changes in important files by calculating and comparing their hash values using the `hashlib` library. It helps ensure file integrity and detect unauthorized or accidental modifications.

## 📁 Project Structure

FileMonitorProject/

├── file_integrity_monitor.py # Main Python script

├── config.ini # Sample config file

├── important.txt # Sample monitored file

├── hash_store.json # Auto-generated hash store (ignored in Git)

└── .gitignore # Excludes the hash_store.json

## ⚙️ How It Works

1. On first run, the script scans all files in the folder and stores their hash values.
2. On each subsequent run, it compares the current hash with the stored one.
3. If a file is modified, added, or deleted, it logs the change to the console.

## ✅ Features

- Detects file modifications
- Detects new files
- Detects deleted files
- Uses SHA-256 hashing for integrity checking

## 🚀 Usage

📦 Requirements
Python 3.x

No external libraries required — uses built-in hashlib and os.

🙈 .gitignore
We recommend ignoring hash_store.json to avoid storing machine-specific data in Git.

hash_store.json

### Clone the repo or download the files:
```bash
git clone https://github.com/yourusername/file-integrity-monitor.git
cd file-integrity-monitor
```
Run the script:
python file_integrity_monitor.py

### 🧪 Example Output
Before modifying a file:

![Image](https://github.com/user-attachments/assets/214ae41d-f4f0-49f2-b469-c92c9fb0de41)

#### |Add or remove some contents inside the txt file|

After modifying a file:

![Image](https://github.com/user-attachments/assets/f33c852f-e3b4-486d-89d6-708988cca7dd)

---
### 🧑‍💻 Author
Name: Bhuvanesh

CodTech Intern
