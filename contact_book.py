import streamlit as st
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
def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    st.success("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        st.warning("No contacts found.")
    else:
        for c in contacts:
            st.write(f"**Name:** {c['name']}, **Phone:** {c['phone']}, **Email:** {c['email']}")

# Delete a contact by name
def delete_contact(name_to_delete):
    contacts = load_contacts()
    contact_found = False
    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            contacts.remove(contact)
            contact_found = True
            break

    if contact_found:
        save_contacts(contacts)
        st.success(f"Contact '{name_to_delete}' deleted successfully!")
    else:
        st.warning(f"Contact '{name_to_delete}' not found.")

# Streamlit UI
st.title("Contact Book")

menu = st.sidebar.selectbox("Select Option", ["Add Contact", "View Contacts", "Delete Contact"])

if menu == "Add Contact":
    st.subheader("Add a New Contact")
    name = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number")
    email = st.text_input("Enter Email")

    if st.button("Add Contact"):
        if name and phone and email:
            add_contact(name, phone, email)
        else:
            st.warning("Please fill in all the fields.")

elif menu == "View Contacts":
    st.subheader("View All Contacts")
    view_contacts()

elif menu == "Delete Contact":
    st.subheader("Delete a Contact")
    name_to_delete = st.text_input("Enter Name of Contact to Delete")

    if st.button("Delete Contact"):
        if name_to_delete:
            delete_contact(name_to_delete)
        else:
            st.warning("Please enter a name to delete.")
