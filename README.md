# Brutedict

Brutedict is a dictionary maker for password bruteforce/dictionary attacks.

It works simply:

You run Brutedict.py onn python3 and you will se de following menu:


```
 ____             _           _ _      _   
| __ ) _ __ _   _| |_ ___  __| (_) ___| |_ 
|  _ \| '__| | | | __/ _ \/ _` | |/ __| __|
| |_) | |  | |_| | ||  __/ (_| | | (__| |_ 
|____/|_|   \__,_|\__\___|\__,_|_|\___|\__|
                                           

Welcome to Brutedict! Choose your option: 
1 - Normal Dictionary maker (Mixes the keywords and nothing more)
2 - Custom separated words (This mixes de keywords with separators you that you have to choose 
* - The format of the Dictionary would be like these: keyword(separator)keyword(separator)keyword 


```
Now, you have to choose which type of dictionary you want.

The dictionary formats are those(in order):

## Normal 

```
AAA0
AAA1
AAA2
AAA3
AAA4
...
AAABBB94
AAABBB95
AAABBB96
AAABBB97
AAABBB98
AAABBB99
...
AAABBBCCC53
AAABBBCCC54
AAABBBCCC55
AAABBBCCC56
AAABBBCCC57
...
CCCCCCCCC96
CCCCCCCCC97
CCCCCCCCC98
CCCCCCCCC99
```
## With separators

```
aaa,aaa
aaa,bbb
aaa,ccc
bbb,aaa
bbb,bbb
bbb,ccc
...
aaa,aaa,aaa
aaa,aaa,bbb
aaa,aaa,ccc
aaa,bbb,aaa
aaa,bbb,bbb
aaa,bbb,ccc
...
aaa/aaa/aaa
aaa/aaa/bbb
aaa/aaa/ccc
aaa/bbb/aaa
aaa/bbb/bbb
aaa/bbb/ccc
aaa/ccc/aaa
aaa/ccc/bbb
aaa/ccc/ccc
bbb/aaa/aaa
...
ccc/bbb/bbb
ccc/bbb/ccc
ccc/ccc/aaa
ccc/ccc/bbb
ccc/ccc/ccc

```

Then answer the following questions:

```
Enter the title of dictionary: dictionary
Enter all the keywords separated by , :aaa,bbb,ccc

```

# Tips
* 1 Keyword don't have to be one word. 'Hello world' will be considered as one keyword

* 2 You don't have to name the dictionary with the .txt end. Brutedict will define de extension.

* 3 You can add numbers as keywords.
# For a better experience
I recommend you to install pyfiglet, it's not mandatory, but the visual experience will be better.

python3 -m pip install pyfiglet

pip3 install pyfiglet