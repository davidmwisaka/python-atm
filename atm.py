# Simple ATM Program

# STEP 1: Set up variables
pin = 1234
balance = 100000
attempts = 0

# STEP 2: Ask for the PIN
while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts += 1
        tries_left = 3 - attempts
        print(f"Incorrect PIN. You have {tries_left} tries left.")

# Stop the program if the PIN is entered incorrectly 3 times
if attempts == 3:
    print("Card blocked!")
else:

    # STEP 3: Continuous ATM menu
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        # STEP 4: Handle menu choices

        # Check balance
        if choice == "1":
            print(f"Your current balance is: {balance}")

        # STEP 5: Deposit
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print(f"Deposit successful!")
                print(f"Your new balance is: {balance}")
            else:
                print("Error: Deposit amount must be greater than zero.")

        # STEP 5: Withdraw
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Error: Enter an amount greater than 0.")
            elif amount > balance:
                print("Error: You do not have enough money!")
            else:
                balance -= amount
                print("Cash dispensed!")
                print(f"Your new balance is: {balance}")

        # Exit
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        # Invalid option
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")