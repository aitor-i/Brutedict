def dictionary_maker_separated():
    title = input("Enter dictionary title: ")
    Dictionary = open(title + ".txt", "w")
    RawWordList = str(input("Enter the key words separated by , :"))
    WordList = RawWordList.split(",")
    RawSeparators = str(input("Enter the separators separated by space letter : "))
    Separators = RawSeparators.split()

    l = len(WordList)

    def CombinationsAndSeparators(separator):

        p = 0
        n = 0
        while l > n:
            for p in WordList:
                Dictionary.write(WordList[n] + separator + p + "\n")
            n = n + 1
        q = 0
        n = 0
        p = 0
        while l > q:
            n = 0
            while l > n:
                p = 0
                while l > p:
                    Dictionary.write(WordList[q] + separator + WordList[n] + separator + WordList[p] + "\n")
                    p = p + 1
                n = n + 1
            q = q + 1

    for i in Separators:
        CombinationsAndSeparators(i)

    Dictionary.close()

    print("Done!")

