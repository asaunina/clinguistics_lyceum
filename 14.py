while True:
    a = input()
    b = input()
    true1 = 0
    true2 = 0
    true3 = 0
    true4 = 0
    for i in range (len(a)):
        if "0" <= a[i] <= "9":
            print("Wrong answer")
            break
        else:
            if "a" <= a[i] <= "z" or "A" <= a[i] <= "Z":
                true1 = true1 + 1
            elif "à" <= a[i] <= "ÿ" or "À" <= a[i] <= "ß":
                true2 = true2 + 1
    for i in range (len(b)):
        if "0" <= b[i] <= "9":
            print("Wrong answer")
            break
        else:
            if "a" <= b[i] <= "z" or "A" <= b[i] <= "Z":
                true3 = true3 + 1
            elif "à" <= b[i] <= "ÿ" or "À" <= b[i] <= "ß":
                true4 = true4 + 1
    if true1 == len(a) and true4 == len(b):
        print("Русское слово-", b)
        print("The English word is", a)
    elif true2 == len(a) and true3 == len(b):
        print("Русское слово -", a)
        print("The English word is", b)
    else:
        print("Wrong answer")
    break
