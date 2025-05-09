import os
from datetime import datetime

def menu():
    print("""
Welcome to your Personal Diary!
--------------------------------
Features:
1. Add a new diary entry (with date and time).
2. View previous entries.
3. Edit an existing entry.
4. Delete an entry.
5. Exit.
""")

def load_entries():
    if os.path.exists("diary.txt"):
        with open("diary.txt", "r") as file:
            entries = file.readlines()
        return [entry.strip() for entry in entries]
    return []

def save_entries(entries):
    with open("diary.txt", "w") as file:
        for entry in entries:
            file.write(entry + "\n")

def add_entry():
    print("\n--- Add a New Diary Entry ---")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Write your entry: ")
    new_entry = f"{date_time} - {entry}"
    entries = load_entries()
    entries.append(new_entry)
    save_entries(entries)
    print("Entry saved successfully!")

def view_entries():
    print("\n--- View Diary Entries ---")
    entries = load_entries()
    if not entries:
        print("No entries found!")
    else:
        for i, entry in enumerate(entries, 1):
            print(f"{i}. {entry}")

def edit_entry():
    print("\n--- Edit a Diary Entry ---")
    entries = load_entries()
    if not entries:
        print("No entries found to edit!")
        return
    view_entries()
    try:
        entry_number = int(input("\nEnter the number of the entry to edit: "))
        if entry_number < 1 or entry_number > len(entries):
            print("Invalid entry number!")
            return
        new_text = input("Write the new text for this entry: ")
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entries[entry_number - 1] = f"{date_time} - {new_text}"
        save_entries(entries)
        print("Entry updated successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def delete_entry():
    print("\n--- Delete a Diary Entry ---")
    entries = load_entries()
    if not entries:
        print("No entries found to delete!")
        return
    view_entries()
    try:
        entry_number = int(input("\nEnter the number of the entry to delete: "))
        if entry_number < 1 or entry_number > len(entries):
            print("Invalid entry number!")
            return
        deleted_entry = entries.pop(entry_number - 1)
        save_entries(entries)
        print(f"Entry deleted successfully: {deleted_entry}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def personal_diary():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting Personal Diary. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

personal_diary()
