pin = "2005"
balance = 500000000  
user_pin = input("Enter your pin: ")
if user_pin == pin:
    print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"You have withdrawn: {amount}")
            print(f"Your new balance is: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print(f"You have deposited: {amount}")
        print(f"Your new balance is: {balance}")
    elif choice == "4":
        print("Thank you for using our ATM.")
    else:
        print("Invalid choice. Please try again.")
else:
    print("Invalid pin. Please try again.")
