def sum(numberOne, numberTwo):
    return numberOne + numberTwo

def subtract(numberOne, numberTwo):
    return numberOne - numberTwo

def multiply(numberOne, numberTwo):
    return numberOne * numberTwo

def divide(numberOne, numberTwo):
    if numberTwo == 0:
        return "Error: Division by zero"
    else:
        return numberOne / numberTwo

def show_results(numberOne,numberTwo, function_sum):
    result_sum = function_sum(numberOne, numberTwo)
    result_subtraction = subtract(numberOne, numberTwo) 
    result_multiplication = multiply(numberOne, numberTwo)
    result_division = divide(numberOne, numberTwo)

    print(f"The sum of {numberOne} and {numberTwo} is {result_sum}")
    print(f"The difference of {numberOne} and {numberTwo} is {result_subtraction}")
    print(f"The multiplication of {numberOne} and {numberTwo} is {result_multiplication}")
    print(f"The division of {numberOne} and {numberTwo} is {result_division}")


show_results(10,10, sum)


