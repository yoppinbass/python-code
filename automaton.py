class Dfa():
    states = []
    initial = ""
    finals = []
    alphabet = []
    transfunc = dict()
    def __init__(self, name):
        self.name = name

    def set_states(self, states):
        self.states = states

    def set_initial(self, initial):
        if (initial in self.states):
            self.initial = initial
        else:
            print("this initial state is not included the states")

    def set_finals(self, finals):
        for final in finals:
            if (final not in self.states):
                print("Error")
                return
        self.finals = finals

    def set_transfunc(self, transfunc):
        self.transfunc = transfunc

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def show_states(self):
        print("\n states, \033[4minitial\033[0m, \033[34mfinal\033[0m")
        for i, state in enumerate(self.states):
            if (state == self.initial and \
                    state in self.finals):
                print("  {0}:{1}" .format(i+1,
                    blue(underline(state))), end="")
            elif (state == self.initial):
                print("  {0}:{1}" .format(i+1,
                    underline(state)), end="")
            elif (state in self.finals):
                print("  {0}:{1}" .format(i+1,
                    blue(state)), end="")
            else:
                print("  {0}:{1}" .format(i+1,
                    state), end="")
        print("\n")

    def show_alphabet(self):
        print(" alphabet: ", end="")
        for letter in self.alphabet:
            print("{} ".format(green(letter)), end="")
        print()

    def show_transfunc(self):
        print('\n transfunc')
        for state in self.states:
            for letter in self.alphabet:
                print("  {0}, {1} -> {2}".format(
                    state,
                    green(letter),
                    self.transfunc[state][letter]))

    def info(self):
        self.show_states()
        self.show_alphabet()
        self.show_transfunc()

    def process(self, sentence):
        print('processing "' + sentence + '"...')
        for letter in sentence:
            if (letter not in self.alphabet):
                print('invalid sentence....')
                return

        current = self.initial
        print('first', current, end="")
        for letter in sentence:
            current = self.transfunc[current][letter]
            print("->{}".format(current), end="")
        print()
        if (current in self.finals):
            print('accepted')
        else:
            print('rejected')

def green(string):
    return "\033[32m" + string + "\033[0m"

def blue(string):
    return "\033[34m" + string + "\033[0m"

def underline(string):
    return "\033[4m" + string + "\033[0m"

def main():

    n = int(input('how many states?: ').rstrip())
    m = Dfa("deterministic finite automaton")

    states = ["q" + str(i+1) for i in range(n)]
    # states = []
    # for i in range(n):
    #     states.append("q" + str(i+1))
    m.set_states(states)

    m.show_states()
    initial_n = int(input('which is the initial state?: ').rstrip()) -1
    m.initial = m.states[initial_n]
    m.show_states()
    while (True):
        flag = str(input('choose final state(q to quit): '))
        if (flag in ["q", "Q", ""]):
            break
        n = int(flag) - 1
        if (n < len(m.states)):
            if (m.states[n] in m.finals):
                m.finals.remove(m.states[n])
            else:
                m.finals.append(m.states[n])
            m.show_states()
        else:
            print('invalid argument')
    alphabet_str = str(input("Enter alphabet(comma separated)\n")).rstrip()
    m.alphabet = alphabet_str.split(",")
    m.show_alphabet()

    m.show_states()
    for state in m.states:
        m.transfunc.__setitem__(state, {})
        for letter in m.alphabet:
            print("{0},{1} -> ".format(state, letter), end="")
            next = int(input()) - 1
            m.transfunc[state].__setitem__(letter, m.states[next])
    m.info()

    while (True):
        input_string = input("Enter a string(q to quit): ")
        if (input_string in ("q", "Q", "")):
            break
        m.process(input_string)



if __name__ == "__main__":
    main()
