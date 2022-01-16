#zakladne cvicenia
#print('ahoj svet')
#print(3, 4, 5)
#print('1','2','3')
#print('what', 'a' 'beautiful' , 'day' , sep=',')
#import this
#x = 2 + 2
#print(type(x))
#y = 2 + 2.
#print(type(y))
#xy = 4/2
#print(type(xy))
#yy = 4/3
#print(type(yy))

#listnumbers = [5, 6, 8, 9, 25]
#print('priemer =' , sum(listnumbers) / len (listnumbers))

#
#x = not ("asd" == "qwe")
#print(x)

#num = 3
#num = num +4
#print(num)

#x = 0
#while x < 5:
# x = x + 1
#print(x)
#def sum_up(x, y):
#   return x + y

#import json_txt
#def zmen (x) :
#    x [0] = 30
#a = [1, 2, 3]
#print(a)
#zmen(a)
#print(a)
#class Calculator:
#    def __init__(self, initial_value):
#        self.current_value = initial_value
#        self.results_history = []

#    def add(self, x):
#        self.results_history.append(self.current_value)
#        self.current_value += x

#    def divide(self, x):
#        if x == 0:
#            return False

#        self.results_history += [self.current_value]
#        self.current_value /= x
#        return True

#    def subtract(self, x):
#        self.results_history += [self.current_value]
#        self.current_value -= x

#    def multiply(self, x):
#        self.results_history += [self.current_value]
#        self.current_value = self.current_value * x

#    def undo(self):
#        if not self.results_history:
#            self.current_value = 0
#        else:
#            self.current_value = self.results_history.pop()

    # self.current_value = self.results_history.pop() if self.results_history else 0

#def alice_cats(number_of_cats):
#    if number_of_cats == 1:
#        cat_string = 'a cat'

#    if number_of_cats>20 and number_of_cats<10 and number_of_cats % 10 in {2, 3, 4}:
#        cat_string = 'cats'

#    else:
#        cat_string = 'cats'

#    return f'Alice has {number_of_cats} ' + cat_string + '.'


#print(alice_cats(14))


#import random

#def repated_myself():
#    set_numbers = set()

#    for i in range(10):
#        number = random.randint(0,10)
#        set_numbers.add(number)

#    if len(set_numbers) < 10:
#        print('Oh no I repeated myself!')

#repated_myself()

#tensor = [[[1,2,3],[1,2,3],[1,2,3]],
#          [[1,2,3],[1,2,3],[1,2,3]],
#          [[1,2,3],[1,2,3],[1,2,3]]]

#def flatten_tensor(tensor):
#    flatten = []

#    for matrix in tensor:
#        for row in matrix:
#            for element in row:
#                flatten.append(element)

#    return flatten

#print(flatten_tensor(tensor))

#radius1 = 32
#radius2 = 36
#price1 = 15
#price2 = 20

#def circle_area_to_price(radius, price):

#    pi = 3.14
#    area = pi * radius * radius
#    return area/price

#print(circle_area_to_price(radius1, price1))
#print(circle_area_to_price(radius2, price2))



#1 Napis program , ktory zobrzi vsetky priridene cisla od 0 do  100
#for x in range(51):
#    if (x == 0 or x==50):
#        continue
#    print(x,end=' ')
#print("\n")

#2 Napíšte program, ktorý zobrazí všetky párne čísla od 0 do 100.
#start, end = 1, 100
#for num in range(start, end + 1):


#    if num % 2 == 0:
#        print(num, end=" ")

#3 Napíšte program, ktorý zobrazí druhé mocniny všetkých celých čísel medzi 0 a 10.

#def printValues():
#    l = list()
#    for i in range(0, 10):
#        l.append(i ** 2)
#    print(l)
#printValues()

#4 Pomocou slučky napíšte čísla od -20 do 20. Potom napíšte: - prvých 6 čísel
#posledných 6 čísel
#všetky párne čísla
#všetky čísla okrem číslice 5
#všetky čísla po číslicu 7 vrátane
#všetky čísla deliteľné 3
#súčet všetkých čísel
#súčet čísel väčších alebo rovných 4
#všetky čísla a ich právomoci
#všetky čísla a ich hodnoty pre modulo 10
#for i in range (-20, 20, 2):
#    print(i)

#cislo = int (input('zadaj cislo :'))
#print(cislo // 10, cislo % 10)
#print(cislo // 100, cislo % 100)
#print(cislo // 1000, cislo % 1000)
#print(cislo // 10000, cislo % 10000)

#dni = 365*12 + 8*30 + 21
#print('pocet dni je', dni)
#hodin = dni * 24
#sekund = hodin * 3600
#print('pocet hodin je', hodin)
#print('pocet sekund je', sekund)

#for i in range (5):
# print(i)
# print('Konec tohoto kola cyklu')

#print("Zdvojnásobovač!")
#cislo = float(input("Zadajte číslo: ")) # reťazec z input () sa prevedie na celé číslo
#print("Jeho dvojnásobok je:", 2 * cislo)
#input()

print("Vitajte v kalkulačke\n")
prvni_cislo = float(input("Zadajte prvé číslo: "))
druhe_cislo = float(input("Zadajte druhé číslo: "))
print("Súčet:", prvni_cislo + druhe_cislo)
print("Rozdiel:", prvni_cislo - druhe_cislo)
print("Súčin:", prvni_cislo * druhe_cislo)
print("Podiel:", prvni_cislo / druhe_cislo)
input("\nĎakujem za použitia kalkulačky, aplikáciu ukončíte ľubovoľnou klávesou.")