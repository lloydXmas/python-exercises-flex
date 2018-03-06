#1. Sum the Numbers
mylist = [16, 35, 6, 7, 3, 22, 12, 52, 21, 30, 5, 10]
mysum = 0
for number in mylist:
    mysum += number
print(mysum)


#2. Largest Number
mylist.sort()
largest = mylist[-1]
print(largest)


#3. Smallest Number
smallest = mylist[0]
print(smallest)


#4. Even Numbers
for number in mylist:
    if number % 2 == 0:
        print(number)


#5. Positive Numbers
mylist = [23, -5, 16, -2, -8, 42, -33, 7, 2, 11, -12, 34]
for number in mylist:
    if number >= 0:
        print(number)


#6. Positive Numbers II
mylist = [23, -5, 16, -2, -8, 42, -33, 7, 2, 11, 12, 34, -20]
positive_list = []
for number in mylist:
    if number >= 0:
        positive_list.append(number)
print(positive_list)


#7. Multiply a list
mylist = [20, 15, 3, 18, 3, 12, 10, 12, 6, 22]
factor_list = []
factor = 5
for number in mylist:
    factor_list.append(number * factor)
print(factor_list)


#8. Multiply Vectors
first_list = [4, 10, 7]
second_list = [3, 6, 7]
third_list = []
position = 0
for position in range(0,3):
    third_list.append(first_list[position] * second_list[position])
print(third_list)
