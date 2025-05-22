def deposit():
    while True: 
        amount_str = input("Please enter the amount that you would like to deposit: ")

        
        try:
            amount = float(amount_str) 
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 10 or 10.50).")

    print(f"You deposited: {amount}")


deposit()