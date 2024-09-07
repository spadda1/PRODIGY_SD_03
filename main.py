from contact_manager import ContactManager

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    manager = ContactManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
            print("Contact added successfully.")
            
        elif choice == '2':
            manager.view_contacts()
            
        elif choice == '3':
            name = input("Enter contact name to edit: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            manager.edit_contact(name, phone if phone else None, email if email else None)
            print("Contact updated successfully.")
            
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)
            print("Contact deleted successfully.")
            
        elif choice == '5':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
