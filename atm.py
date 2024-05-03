from art import text2art
from datetime import date

# Function to display ASCII art for "ATM MACHINE"
print(text2art("ATM MACHINE"))

atm_pin = "1234"
global balance

# Function to get the current date
def todayDate():
    today = date.today()
    return today.strftime("%d/%m/%Y")

# Function to check the balance
def checkBalance(balance):
    print(f"The current balance is: {balance}")

# Function to withdraw amount
def withdrawAmount(balance):
    while True:
        withdraw = int(input("Enter withdraw amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"An amount of INR {float(withdraw)} has been DEBITED from your account XXXX0709 on {todayDate()}. Total Avail.bal INR {balance}")
            break
        else:
            print("Insufficient Balance")
    return balance

# Function to deposit amount
def depositAmount(balance):
    deposit = int(input("Enter deposit amount: "))
    balance += deposit
    print(f"An amount of INR {float(deposit)} has been CREDITED to your account XXXX0709 on {todayDate()}. Total Avail.bal INR {balance}")
    return balance

# Main function to handle user interactions
def main():
    user_pin = input("Enter your pin: ")
    if user_pin == atm_pin:
        print("1. Check Balance\n2. Withdraw Amount\n3. Deposit Amount\n4. Exit")
        balance = 2000
        while True:
            choice = input("Enter your Choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    checkBalance(balance)
                elif choice == 2:
                    balance = withdrawAmount(balance)
                elif choice == 3:
                    balance = depositAmount(balance)
                elif choice == 4:
                    print("Thank You Visit Again ⭐⭐⭐")
                    break
                else:
                    print("Invalid Choice. Please enter a valid option.")
            else:
                print("Invalid Input. Please enter a valid number for choice.")

    else:
        print("Invalid PIN / Wrong PIN")
        main()

if __name__ == "__main__":
    main()