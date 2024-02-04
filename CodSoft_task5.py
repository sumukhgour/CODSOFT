class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            self.contacts[name] = {
                'phone_number': phone_number,
                'email': email,
                'address': address
            }
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists. Please choose a different name.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']}")

    def search_contact(self, search_term):
        matching_contacts = {
            name: details for name, details in self.contacts.items()
            if search_term.lower() in name.lower() or search_term in details['phone_number']
        }

        if not matching_contacts:
            print(f"No contacts found for '{search_term}'.")
        else:
            print("Matching Contacts:")
            for name, details in matching_contacts.items():
                print(f"{name}: {details['phone_number']}")

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                'phone_number': phone_number,
                'email': email,
                'address': address
            }
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the contact name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == "4":
            name = input("Enter the contact name to update: ")
            phone_number = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            contact_manager.update_contact(name, phone_number, email, address)

        elif choice == "5":
            name = input("Enter the contact name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
