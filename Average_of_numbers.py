'''total_num = int(input("How many numbers u want to find avg ?"))
print(total_num)
numbers = []
for i in range(0, total_num):
    element = int(input("enter numbers: "))
    numbers.append(element)
total = sum(numbers)
avg = total/total_num
print("average is: ", avg)
'''

#Another solution

t_num = int(input("how many num: "))
print(t_num)
sum = 0
for i in range(0,t_num):
    element = int(input("enter numbers: "))
    sum = sum + element
    print(sum)
avg = sum/t_num
print("avg is: ", avg)
