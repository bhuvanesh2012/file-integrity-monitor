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

### 1. Clone the repo or download the files:
```bash
git clone https://github.com/yourusername/file-integrity-monitor.git
cd file-integrity-monitor

Run the script:
  python file_integrity_monitor.py

Example Output
      === File Integrity Monitor ===
    [INFO] New file added to monitoring: important.txt
    [INFO] New file added to monitoring: config.ini

    # After modifying a file:
    [ALERT] File modified: important.txt

#### 📄 License
This project is for educational use as part of an internship task.

##### 🧑‍💻 Author
Bhuvanesh
Intern at CodTech
