
num = int(input("Enter a number: "))

original = num

n = len(str(num))

# Calculate sum of powers
result = 0

while num > 0:
    digit = num % 10
    result += digit ** n
    num //= 10

# Check condition
if result == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")




#challenge extension
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    n = len(str(num))
    temp = num
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** n
        temp //= 10

    if result == num:
        print(num)
