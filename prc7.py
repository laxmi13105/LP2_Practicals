# Elementary Chatbot for Customer Interaction

print("===================================")
print("      CUSTOMER SUPPORT CHATBOT     ")
print("===================================")

name = input("Enter your name: ")

print("\nHello", name, "!")
print("How can I help you today?")

while True:

    print("\nChoose an option:")
    print("1. Product Information")
    print("2. Order Status")
    print("3. Return Policy")
    print("4. Customer Care Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Product Information
    if choice == "1":

        print("\nOur products include:")
        print("- Laptop")
        print("- Mobile")
        print("- Headphones")
        print("- Smart Watch")

    # Order Status
    elif choice == "2":

        order_id = input("Enter your Order ID: ")

        print("Order ID", order_id, "is currently SHIPPED.")

    # Return Policy
    elif choice == "3":

        print("\nReturn Policy:")
        print("Products can be returned within 7 days.")

    # Customer Care
    elif choice == "4":

        print("\nCustomer Care Number: 9876543210")
        print("Email: support@gmail.com")

    # Exit
    elif choice == "5":

        print("\nThank you for using our chatbot!")
        break

    # Invalid Choice
    else:

        print("\nInvalid choice! Please try again.")