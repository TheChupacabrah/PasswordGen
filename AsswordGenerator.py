#Password Generator
#February 23 2022
#John Hatch
from random import randint
from time import sleep
#random password variables
num = ["1","2","3","4","5","6","7","8","9","0"]
sym = ["!", "@", "#", "$", "%", "^", "&", "*", "=", "+"]
let = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
cap = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


choice = int(input("Welcome to the password generator, how many characters do you need? "))
total = []

#generator a character
def ran_char(num, sym, let, cap):
    charnum = num[randint(0, len(num)-1)]
    charsym = sym[randint(0, len(sym)-1)]
    charlet = let[randint(0, len(let)-1)]
    charcap = cap[randint(0, len(cap)-1)]
    ranchar = (charnum, charsym, charlet, charcap)
    char = ranchar[randint(0, len(ranchar) -1)]
    return char

for x in range(choice):
    total.append(ran_char(num,sym,let,cap))
    
for x in total:
    print(x, end="")
