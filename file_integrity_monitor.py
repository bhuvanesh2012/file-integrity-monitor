import hashlib
import os
import json

HASH_STORE = "hash_store.json"

def calculate_hash(filepath):
    try:
        with open(filepath, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None

def load_hashes():
    if os.path.exists(HASH_STORE):
        with open(HASH_STORE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=4)

def check_file(filepath):
    stored_hashes = load_hashes()
    current_hash = calculate_hash(filepath)

    if not current_hash:
        return

    if filepath in stored_hashes:
        if stored_hashes[filepath] == current_hash:
            print(f"[OK] No change in {filepath}")
        else:
            print(f"[ALERT] File modified: {filepath}")
    else:
        print(f"[INFO] New file added to monitoring: {filepath}")

    stored_hashes[filepath] = current_hash
    save_hashes(stored_hashes)

# Example usage
if __name__ == "__main__":
    print("=== File Integrity Monitor ===")
    file_list = ["important.txt", "config.ini"]  # Add file names here
    for file in file_list:
        check_file(file)