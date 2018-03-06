#1. Uppercase a String
mystring = 'uppercase'
for char in mystring:
    print(char.upper(), end = '')
print('')


#2. Capitalize a String
mystring = 'capitalize'
for char in mystring:
    print(char.capitalize(), end = '')
print('')


#3. Reverse a String
mystring = 'reverse'
count = -1
for char in mystring:
    print(mystring[count], end = '')
    count -= 1
print('')


#4. Leetspeak
mystring = 'aenean lacinia bibendum nulla sed consectetur. Donec ullamcorper nulla non metus auctor fringilla'
for char in mystring:
    if char == 'a':
        print('4', end = '')
    elif char == 'a':
        print('4', end = '')
    elif char == 'e':
        print('3', end = '')
    elif char == 'g':
        print('6', end = '')
    elif char == 'i':
        print('1', end = '')
    elif char == 'o':
        print('0', end = '')
    elif char == 's':
        print('5', end = '')
    elif char == 't':
        print('7', end = '')
    else:
        print(char, end = '')
print('')


#5. Long-long chars
lstring = 'Cheese'
for char in range(len(lstring)):
    if lstring[char] == lstring[char-1]: #look-behind, since char+1 produces "index out of range" error
        print(lstring[char]*5, end = '')
    else:
        print(lstring[char], end = '')
print('')


#6. Caesar Cipher
alpha = 'abcdefghijklmnopqrstuvwxyz'
phrase = 'lbh zhfg hayrnea jung lbh unir yrnearq'
for i in range(len(phrase)):
    if phrase[i] == " ":
        print(" ", end = '')
    for x in alpha:
        if phrase[i] == x:
            newletter = alpha.index(x)+13
            if newletter >= 26:
                newletter -= 26
            print(alpha[newletter], end = '')
print('')
