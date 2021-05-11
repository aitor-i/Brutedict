from dictionaries.normal import dictionary_maker
from dictionaries.separated import dictionary_maker_separated
try:
    import pyfiglet

except:
    print('Pyfigilet not imported')

class Switcher:

    def switch(self, option):

        default = 'Invalid option'

        return getattr(self, 'Case_'+str(option), lambda:default)()

    def Case_1(self):

         dictionary_maker()



    def Case_2(self):

         dictionary_maker_separated()



menu = Switcher()
try:
    result = pyfiglet.figlet_format("Brutedict")
    print(result)
except:
    print('Brutedict')

while 1 == 1:
    print('Welcome to Brutedict! Choose your option: \n'
          '1 - Normal Dictionary maker (Mixes the keywords and nothing more)\n'
          '2 - Custom separated words (This mixes de keywords with separators you that you have to choose \n'
          '* - The format of the Dictionary would be like these: keyword(separator)keyword(separator)keyword \n')
    choose = input()
    if choose == '1':
        menu.switch(1)
        break
    elif choose == '2':
        menu.switch(2)
        break


