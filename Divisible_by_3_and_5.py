num = int(input("enter a number: "))
print(num)
if num % 3 == 0:
    print("number is divisible by 3")
    if num % 5 == 0:
        print("number is divisible by 5")
if num %3 == 0 and num % 5 == 0:
    print("nuber is divisible by 3 and 5")
else:
    print("i dont know")
