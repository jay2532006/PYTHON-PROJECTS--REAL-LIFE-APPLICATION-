import os
from cryptography.fernet import Fernet

if not os.path.exists("key.key"):
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)
password_file = "passwords.txt"

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def save_password(service, username, password):
    encrypted_password = encrypt_password(password)
    with open(password_file, "a") as file:
        file.write(f"{service},{username},{encrypted_password}\n")
    print(f"Password for {service} saved successfully.")

def search_password(service):
    if not os.path.exists(password_file):
        print("No passwords stored yet.")
        return
    with open(password_file, "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service == service:
                password = decrypt_password(encrypted_password)
                print(f"Service: {stored_service}\nUsername: {username}\nPassword: {password}")
                return
    print("Service not found.")

def update_password(service, new_password):
    if not os.path.exists(password_file):
        print("No passwords stored yet.")
        return
    updated = False
    lines = []
    with open(password_file, "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service == service:
                encrypted_password = encrypt_password(new_password)
                updated = True
                print(f"Password for {service} updated successfully.")
            lines.append(f"{stored_service},{username},{encrypted_password}\n")
    with open(password_file, "w") as file:
        file.writelines(lines)
    if not updated:
        print("Service not found.")

def delete_password(service):
    if not os.path.exists(password_file):
        print("No passwords stored yet.")
        return
    deleted = False
    lines = []
    with open(password_file, "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service != service:
                lines.append(line)
            else:
                deleted = True
    with open(password_file, "w") as file:
        file.writelines(lines)
    if deleted:
        print(f"Password for {service} deleted successfully.")
    else:
        print("Service not found.")

def display_menu():
    print("\nPassword Manager")
    print("1. Save a new password")
    print("2. Search for a password")
    print("3. Update a password")
    print("4. Delete a password")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        service = input("Enter service name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        save_password(service, username, password)
    elif choice == "2":
        service = input("Enter service name: ")
        search_password(service)
    elif choice == "3":
        service = input("Enter service name: ")
        new_password = input("Enter new password: ")
        update_password(service, new_password)
    elif choice == "4":
        service = input("Enter service name: ")
        delete_password(service)
    elif choice == "5":
        print("Exiting Password Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
