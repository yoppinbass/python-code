def color(string, color):
    colors = ["black", "red", "green", "yellow",
           "blue", "purple", "skyblue", "white" ]
    if color in colors:
        i = colors.index(color)
        # print(colors.index(color))
        # print("\033[{}m{}\033[0m".format(30+i, string))
        return "\033[{}m{}\033[0m".format(30+i, string)

if __name__ == '__main__':
    text = 'color'
    print('\\033[31m', "{text}", '\\033[0m')
    numbers = [0, 30, 40, 80, 90, 100]
    for i in range(8):
        for number in numbers:
            print("{0}: \033[{0}m{1}\033[0m   ".format(number+i, text), end="")
        print()
    color("hello", "red")
    color("hello", "gold")
