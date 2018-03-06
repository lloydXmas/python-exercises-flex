#1. 1 to 10
for num in range(1, 11):
    print(num)


#2. n to m
start = input("Start from: ")
end = input("End on: ")
for num in range(int(start),(int(end) + 1)):
    print(num)


#3. Odd Numbers
for num in range(1, 11):
    if num % 2 != 0:
        print(num)


#4. Print a Square
for num in range(0,5):
    print('*' * 5)


#5. Print a Square II
square_num = input("How big is the square? ")
for num in range(0, int(square_num)):
    print('*' * int(square_num))


#6. Print a Box
width = int(input("Width? "))
height = int(input("Height? "))
col = width - 2
row = height - 2
print('*' * width)
for num in range(0, row):
    print('*', end = '')
    print(' ' * col, end = '')
    print('*')
print('*' * width)


#7. Print a Triangle
star_size = 14
spaces = (star_size / 2) - 1
for i in range(1, star_size):
    if i % 2 != 0:
        print(' ' * int(spaces), end = '')
        print('*' * i, end = '')
        print(' ' * int(spaces))
        spaces -= 1


#8. Print a Triangle II
height = 20
star_size = height * 2
spaces = (star_size / 2) - 1
for i in range(1, star_size):
    if i % 2 != 0:
        print(' ' * int(spaces), end = '')
        print('*' * i, end = '')
        print(' ' * int(spaces))
        spaces -= 1


#9. Multiplication Table
for x in range(1,11):
    for y in range(1,11):
        mult = x * y
        print("{} x {} = {}".format(x, y, mult))


#Bonus: Print a Banner
banner = input('Text? ')
banner_len = len(banner) + 4
print('*' * banner_len)
print('*', banner, '*')
print('*' * banner_len)


#Bonus: Triangle Numbers
for x in range(1,101):
    i = (x * (x + 1))/2
    print(int(i))
