import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!\n")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
    else:
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
        print()

# Delete a contact by name
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    
    # Check if the contact exists
    contact_found = False
    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            contacts.remove(contact)
            contact_found = True
            break
    
    if contact_found:
        save_contacts(contacts)
        print(f"Contact '{name_to_delete}' deleted successfully!\n")
    else:
        print(f"Contact '{name_to_delete}' not found.\n")

# Main menu
def menu():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

menu()
