

a = 1
b = 2


def check():
    print(a)

def add():
    global a
    a = a + b


def main():
    while a < 10:
        print(a)
        add()
        check()


main()
