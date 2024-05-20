#OctaNet Python Development (April -2024) Intern Group-1

#English is the default language
print("Welcome to OctaNet Python Development ATM\n\n\n   Insert your ATM card")


#defining the parameters
#pin is 7287
password=7287
balance=10000
choice=0
transaction_history = []


#to enter the pin in the atm
pin=int(input("Enter your four digit pin"))

#checking the condition
if pin==password:
    while choice!=6:
        print("***MENU****")
        print("1 = Balance Enquiry ")
        print("2 = Deposit")
        print("3 = Withdraw")
        print("4 = Transfer")
        print("5 = Transaction History ")
        print("6 = cancel\n")

        #enter your option
        choice=int(input("\nEnter your option"))

        #if the customer choice is 1
        if choice==1:
            print("Balance=",balance,"rupees")

        #if the customer choice is 2
        elif choice==2:
            dep=int(input("Enter your Deposit amount"))
            balance+=dep
            print("deposited amount=rupees",dep)
            print("Amount deposited successfully")
            print(" Balance=", balance,"rupees")


        #if the customer choice is 3
        elif choice==3:
            withdraw=int(input("Enter your Withdraw amount"))
            balance-=withdraw
            print("withdraw amount=rupees",withdraw)
            print("Processing...")
            print("collect your cash ")
            print("Amount Withdraw successfully")
            print("Remaining Balance=", balance, "rupees")
            #if withdraw amount greater than balance
            if withdraw > balance:
                print("insufficient balance")


        elif choice == 4:
            transfer_amount = int(input("Enter amount to transfer: "))
            recipient_account = input("Enter recipient's account number: ")
            transaction_history.append(f"Transferred ${transfer_amount} to {recipient_account}")
            print("Transfer successful!")

            # If the customer choice is 5

        elif choice == 5:
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)



    #if the customer choice is 4
        elif choice==6:(
            print("session ended ,Good Bye!"))


            
        #if the customer choice is none
    else:

             print("Invaid entry! Try Again")



#if the customer entered incorrect pin
else:
    print("pin incorrect! Try Again")