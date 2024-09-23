
numberOne = 10;
numberTwo = 20;

sum = numberOne + numberTwo;
print(f"The sum of ${numberOne} and ${numberTwo} is ${sum}")

subtraction = numberOne - numberTwo;
print(f"The difference of ${numberOne} and ${numberTwo} is ${subtraction}")

multiplication = numberOne * numberTwo;
print(f"The multiplication of ${numberOne} and ${ numberTwo} is ${multiplication}")

division = numberOne / numberTwo;
print(f"The division of ${numberOne} and ${ numberTwo}");

remainder = numberOne % numberTwo;
print(f"${numberOne} divided by {numberTwo}: {remainder}")

exponentiation = numberOne ** numberTwo;
print(f"The exponentiation of ${numberOne} to the power of ${numberTwo} is ${exponentiation}")

squareRoot = numberOne ** (1/2);
print(f"The square root of ${numberOne} is ${squareRoot}")

cubeRoot = numberOne ** (1/3);
print(f"The cube root of ${numberOne} is ${cubeRoot}")

factorial = 1;

for i in range(1, numberOne + 1):
    factorial *= i;
print(f"The factorial of ${numberOne} is ${factorial}")