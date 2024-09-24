balance = 1500;
withdraw = 800;

print(balance >= withdraw);
print(balance <= withdraw);
print(balance == withdraw);
print(balance != withdraw);

# Additional Challenge: Calculate the remaining balance after withdrawing the specified amount. 

    # Example:
    # balance = 1500
    # withdraw = 800
    # remaining_balance = 1500 - 800 = 700

    # Output: 700
remaining_balance = balance - withdraw;
print(f"The remaining balance after withdrawing ${withdraw} is ${remaining_balance}");