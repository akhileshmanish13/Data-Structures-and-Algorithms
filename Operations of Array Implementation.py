# Array : collection of similar data type

numbers = [25, 56, 78, 69, 34, 27, 16, 76, 11, 55]

# Randomly  access any value if we know it's  index. INDEXing start from 0
# print(numbers[0])
# print(numbers[1])

# Assign any new value at particular index
numbers[1] = 54
print(numbers[1])
numbers[3]= 22
numbers[4]= 36

# Print new updated list
for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i]);

print(numbers[0:5])

# Minimum number from the list
minimum = numbers[1]

for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)
