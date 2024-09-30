age_user = int(input("Enter your age ? "))

if(age_user >= 18):
    print("Your have age to take you driver license")
elif(age_user < 18 and age_user > 0):
    print("Your age is not eligible to take you driver license")
elif (age_user <= 0):
    print("Invalid age input")
