fruits = {"Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Lemon","Lemon","Lemon"}

print(len(fruits)) # 3
print(fruits)

numbers ={1,2,2,3,4,5,5,6,7,7}
numbersList = list(numbers)
print(numbersList)

for i in numbers:
    print(i)

for index, number in enumerate(numbers):
    print(f"Index: {index}, Number: {number}")