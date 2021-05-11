def dictionary_maker():
    title = input("Enter the title of dictionary: ")
    dictionary = open(title + ".txt", "w")

    RawWordList = input(str("Enter all the keywords separated by , :"))
    WordList = RawWordList.split(",")

    n = 0
    s = 0
    i = 0
    l = 0
    p = 0
    z = 0
    h = 0

    y = len(WordList)
    f = y - 1

    while p != y:
        for z in range(100):
            dictionary.write(WordList[p] + str(z) + "\n")
            z = z + 1
        p = p + 1

    while s != y:
        for l in range(100):
            dictionary.write(WordList[n] + WordList[s] + str(l) + "\n")
            l = l + 1
        s = s + 1

        if s == y:
            s = 0
            n = n + 1

            if n == y:
                break
            else:
                for i in range(100):
                    dictionary.write(WordList[n] + WordList[s] + str(i) + "\n")
                    i = i + 1

                s = s + 1
    s = 0
    n = 0
    h = 0
    while s != y:
        for l in range(100):
            dictionary.write(WordList[h] + WordList[n] + WordList[s] + str(l) + "\n")
            l = l + 1
        s = s + 1

        if s == y:
            s = 0
            n = n + 1
            if n == y:
                n = 0
                h = h + 1
                if h == y:
                    break
                else:
                    dictionary.write(WordList[h] + WordList[n] + WordList[s] + str(i) + "\n")
                    i = i + 1

            else:
                i = 0
                for i in range(100):
                    dictionary.write(WordList[h] + WordList[n] + WordList[s] + str(i) + "\n")
                    i = i + 1

                s = s + 1

    dictionary.close()

    print("Done")
    print("Enjoy it!")


