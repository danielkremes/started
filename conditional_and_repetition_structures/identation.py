def withdraw(withdraw):
    balance = 500
    withdraw = withdraw;
    
    if balance >= withdraw:
        print("Withdrawal successful")
        balance -= withdraw
    else:
        print("Withdrawal unsuccessful")

withdraw(600)