import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for name, info in contacts.items():
        print(f"{name} - {info}")

def edit_contact():
    name = input("Enter name to edit: ")
    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        save_contacts(contacts)
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1.Add 2.View 3.Edit 4.Delete 5.Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
