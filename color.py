text = 'color'
print('\\033[31m', "{text}", '\\033[0m')
numbers = [0, 30, 40, 80, 90, 100]
for i in range(8):
    for number in numbers:
        print("{0}: \033[{0}m{1}\033[0m   ".format(number+i, text), end="")
    print()
