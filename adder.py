def half_adder(x, y):
    c = x & y
    s = x ^ y
    return (c, s)

def full_adder(x, y, z):
    (c1, s1) = half_adder(x, y)
    (c2, s2) = half_adder(s1, z)
    c = c1 | c2
    s = s2
    return (c, s)

def main():
    print('half(0, 0)',half_adder(0, 0))
    print('half(1, 0)',half_adder(1, 0))
    print('half(1, 1)',half_adder(1, 1))

    print('full(0, 0, 0)',full_adder(0, 0, 0))
    print('full(1, 0, 0)',full_adder(1, 0, 0))
    print('full(1, 1, 0)',full_adder(1, 1, 0))

    print('full(0, 0, 1)',full_adder(0, 0, 1))
    print('full(1, 0, 1)',full_adder(1, 0, 1))
    print('full(1, 1, 1)',full_adder(1, 1, 1))

if __name__ == '__main__':
    main()
