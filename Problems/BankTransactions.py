Persons = {}


def deposit(name, value):
    if name in Persons:
        Persons[name] += int(value)
    else:
        Persons[name] = int(value)


def withdraw(name, value):
    if name in Persons:
        Persons[name] -= int(value)
    else:
        Persons[name] = -int(value)


def Balance(name):
    print(Persons[name])


def Transfer(name1, name2, value):
    a1 = name1 in Persons
    if a1 == False:
        Persons[name1] = 0
    a2 = name2 in Persons
    if a2 == False:
        Persons[name2] = 0

    if name1 in Persons and name2 in Persons:
        Persons[name1] -= int(value)
        Persons[name2] += int(value)


def Income(p):
    keys = Persons.keys()
    for i in keys:
        if Persons[i] >= 0:
            t = int(p)
            temp = Persons[i] * t / 100
            Persons[i] += temp


def balance(name):
    #better use try/except here,not if else,because in second case no way to reach code into "else" case
    if name in Persons:
        print(Persons[name])
    else:
        print("Error, there is no such a lent in a bank list")


if __name__ == '__main__':
    while True:
        line = input()
        l = line.split()
        #print(f'{l = }')
        if line == 'exit':
            break
        else:
            if l[0] == "Deposit":
                deposit(l[1], l[2])
            if l[0] == "Income":
                Income(l[1])
            if l[0] == "Balance":
                Balance(l[1])
            if l[0] == "Transfer":
                Transfer(l[1], l[2], l[3])
            if l[0] == "Withdraw":
                withdraw(l[1], l[2])
