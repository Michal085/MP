# numerical_data_types
 # 1 + 1  scitovanie
 # 2 - 2  odcitovanie
 # 3 * 3  nasobenie
 # 20 / 4 delenie  desatine cislo float 
 # 5 // 5 celociselne delenie
 # 6 % 3  zvysok po deleni 
 # abs(-3) 
 #2 ** 2   umocnovanie


 # premenne- Variables
 # do premenej mozme ulozit hocijaky datovy typ 
# premennu mozme definovat aj viac krat
# pozor velke a male pismena niesu to iste 
# nazvy premennych mozu pozostavat len z malych a velkych pismen LEPSIE JE POUZIVAT ANGLICKE NAZVY A _ podtrzniku  
number_cars = 25  
number_employees = 10
print(number_cars + number_employees)

# datove typy boolean
# tento datovy typ ma len dve hodnoty True a False 

true_value = True
false_value = False

# vysledkom porovnavacich operacii je datovy typ 
#3 < 5
#5 > 10
#5 == 7
#4 <= 8
#8 == 8.0
#9 != 10

# na zistenie rovnosti pouzi vzdy dvojite == dovod je ze jedno = sa pouziva pri priradeni premennej 
# porovnavacie operacie vieme aj retazit logickymi operatormi and, or
x = 3 > 4 or 4 > 3
print(x) # TRUE
print(not(x)) # FALSE

# negacia pomocou funkcie not
#Logický súčin a súčasne
#A	B	   A        and           B	 
#False    False               	False	 
#True	  False	                False	 
#False	  True	                False	 
#True	  True	                True	 

#Logický súčet alebo
#A	B	     A       or         B	 
#False	    False	          False	 
#True	    False	          True	 
#False	    True	          True	 
#True	    True	          True	 

#Negácia neplatí
#A	   not      A	 
#False   	   True	 
#True	       False

# while_cycle
# while cyklus ma v sebe podmienku a funguje podobne ako if

counter = 0
while counter <5:
    print(counter)
    counter = counter +1
print("Ahoj")


#Nekonecny while cyklus nikdy podmienka neskonci ak stlacis ctrl + C zastavis nekonecny while cyklus 
counter = 0
while True:
    print(counter)
    if counter >= 4:
        break
    counter +=1
print("Ahoj")


for i in [1, 2, 3, 4]:
    print(i)
    if i ==4:
        break # break vieme pouzit aj na ukoncenie cyklu
print("Ahoj")

counter = 0
while True:
    if counter == 2:
        counter += 1
        continue # klucove slovo continue sa pouziva na predcastne ukoncenie iteracie ale nie celeho cyklu
    if counter >=5:
        break
    print(counter)
    counter += 1

for i in [1, 2, 3, 4, 5]:
    if i == 2:
        continue
    print(i)



# Retazce Strings
# string vieme definovat pomocou dvojitych "" uvodzoviek ale aj jednoduchych ''
string = "priamy vypis stringu"
print(string)
# string, hocijaky datovy tip ale aj premennu vieme vypisat pomocou funkcie print
print(1)
print(1.5)
print(True)
string = 'This is single quote \' in single quote string ' # takto definujeme uvodzovku v stringu plati aj ak chceme dvojitu "
print(string)

string1 = "This is string with \nnew line" # \n je symbolnoveho riadka , vidime ho len pomocou print 
print(string1)

string2 = "This is string with \n\tnew line and tab" # je symbol tabulatoru odsadi nam 4 medzeri 
print(string2)

new_patch = "C:\documents\notes" # co ak nechceme vypisat novy riadok 
print(new_patch)

new_patch = r"C:\documents\notes"  # pomocou r robi ze zmaze ucinost specialneho znaku 
print(new_patch)

#\n - nový riadok
#\t - tabulátor
#\' - apostrof
#\" - úvodzovka
#\\ - opačná lomka

# znakove retazce string_operations
# stringy pozostavaju so znakou nie s pismen a cisiel 

string_concatenation = "Hello" + " " +  "world" #ak chceme medzi Helloworld medzeru tak jednoducho + " " + cize vieme ich aj spajat
print(string_concatenation)

# stringy vieme aj nasobit 
string_multiplication = 3 * "Hi "
print(string_multiplication)

# ak chceme vieme spajat aj string a cislo 
string_exercise = "Number is "
string_exercise_two = 6
print(string_exercise + string_exercise_two) # toto nam vypise chybu ze nemozme scitavat string a integer (cislo)

print(string_exercise + str(string_exercise_two)) # prekastujeme pomocou str premeni cislo na string


# do stringu vieme pristupovat pomocou indexu ktory zacina od 0 a []
name = "Michal Placko"
#       0123456789101112
#                    
print(name[0])
print(name[4])

print(name[0:13]) # vieme pristupovat aj cez zlozeny index 
print(name[0:6])
print(name[-13:])
print(name[:-4])
print(name[- 8:])

# listy LISTS

number_list = [1, 2, 3, 4, 5, 6, 7] # nasledna definicia listu
print(number_list)

# vieme don vkladat akekolvek datove typy
string_list = ["Michal", "Placko", "Paul"]
combinated_list = [1, "Michal", "Paul", True, 2.5]

# index listu je rovnaky ako list indexu stringu 
print(number_list[0])
print(number_list[2:4]) 
print(number_list[0:3])
print(number_list[-1])
print(number_list[-2:])

# listy vieme aj scitavat 
print(number_list + [8, 9, 10, 11])


# listy na rozdiel od stringu vieme upravovat pomocou indexu [] 
best_name ="Michal Placko"
numbers = [0, 1, 2, 3, 4, 5, 6, 7,]
numbers + [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
numbers[0] = 10 # miesto 0 sa zmeni hodnota na 10 
print(numbers)

# upravit vieme aj pomocou zlozeneho indexu 
numbers[1:3]
numbers + [1, 2]
print(numbers)

numbers_lists = [1, 2, 3, 4]
numbers_lists.extend([5, 6, 8, 9]) # Funkcia extend rozbali pole a prida ho nakoniec 
print(numbers_lists)


letters = ['m', 'i', 'c', 'h', 'a', 'l', 'p', 'l', 'a', 'c', 'k', 'o']
print(letters.count('a')) # Funkcia count vrati pocet vyskytu prvku v zatvorke
print(letters.index('c')) # Funkcia index vrati poziciu prveho vyskytu prvku v zatvorke 
letters.insert(3, "x") # Funkcia insert vlozi druhy prvok v zatvorke na poziciu (prvy prvok v zatvorke)
print(letters)

letters.remove("c") # Funkcia remove vymaze prvy vyskyt znatku v zatvorke 
print(letters)

letters.reverse() # Funkcia reverse otoci pole
print(letters) 

letters.clear() # Funkcia clear zmaze cely obsah pola
print(letters)

numbers = [8, 25, 61, 45, 2, 36, 4, 7, 10, 18, 22, 64, 70, 23]
numbers.sort() # Funkcia sort usporiada pole 
print

nums = [1, 2, 3]
nums.pop() # Funkcia pop vrati posledny prvok z pola a zaroven ho z neho vymaze
print(nums)




#Podmienky , CONDITIONS
# jednoducha podmienka . Splni sa ak je vyraz v podmienke pravda , vzdy musime cast vykonania oddelit  but tab alebo 4 medzerami
is_student = True
if is_student == True:
    print("He is a programmer")

is_programmer = True
is_student = True
if is_programmer == False:
    print("He is a programmer")
# ak vyraz nieje pravda tak python vykona kod v casti else
else:
    print("He is not a programmer")

# takto jednoducho vieme retazit podmienky ak neplati if python prejde na druhu elif a ak neplati ani ten prejde na else 
if is_programmer == False:
    print("Is not a programmer")
elif is_student == True:
    print("Is student")
else:
    print("Is programmer and is not a student")

 #for cyklus
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
#print(number)

name = 'Michal'
for character in name:
   print(character)


counter = range(0, 12)
print(list(counter))

def sucet_cisiel (cislo1, cislo2):
    result = cislo1 + cislo2
    return result

x = (5 + 4) +3
sucet = sucet_cisiel(cislo2=4, cislo1 =5)

# Dictionares - Slovniky
my_dict = {
   "key":"value",  # vzdy je na lavo kluc cize key a na pravo hodnota cize value 
   "Michal": 31 ,
   True: "True",
   False: "True",
}
my_dict["Michal"] = 32  # zmena hodnoty pomocou kluca "Michal"
print(my_dict["Michal"])

#print(my_dict)
# k hodnotam vieme pristupovat pomocou [] kluca 
#print(my_dict["Michal"])

# dictionares je mutable sam o sebe takze vieme menit hodnoty a aj ich vymazavat 
#my_dict["Michal"] = 37
#my_dict["Thomas"] = 20

#print(mixed_dict)

person = { 
    "name" : "Michal", 
    "surname": "Placko", 
    "languages": ["Python", "PostgreSQL", "HTML_CSS"],
    "instagram": "@michalplacko",
    "address": {
        "city": "New York",
        "street": "stret_name",
        "street_number": 45
    }

}
print (person["languages"][-1])

for kluc, hodnota in list(person.items()):  # list(item.persons) vrati pole dvojic 
   print("Key is: ", kluc)
   print("Value is: ", hodnota)
   
   
print(list(person.keys())) # funkcia person.keys vrati list klucov
print(list(person.values())) # funkcia vrati list hodnot
person.pop("Michal") # pop vrati hodnotu kluca a nasledne kluc vymaze zo slovnika 
person.popitem() # vrati tuple key-value a vymaze ho zo slovnika  


   
number_list = [1, 2, 3, 4, 8, 3, 29, 51, 79, 35, 78, 101, 114, 151, 156, 748, 14,]
print(number_list[7])

# Tuple je to ako imutable list cize nemozme menit obsah 
 
first_tuple = 1, 2, 3, 4
print(first_tuple)
print(type(first_tuple))

def function_returning_tuple(element1, element2):
    return element1, element2

 x = function_returning_tuple("ahoj", "Michal")
print(x)


# podtrznik znamena zamlcanie prvku 
# 3 ku nevypise
x = (1, 2, 3)
a,b,_ = x 
print(a,b)


# Coments , komenty
"""
Toto je viac riadkovy komentar v pythone. Ktory sa tiez nikdy nevykona.
Takyto komentar sa pouziva na nieco co sa vola docstring.
Docstring specifikuje funkciu pomocou komentaru. 
"""

#def custom_addition(elemnt1, element2):
    """
    Custom addition function dedicated for addition of element1 and element2.

    Parameters:

    element1 (int): First element
    element2 (int): Second element

    Returns:
    
    sum (int): addition
    """
#    return element1 + element2

# Type hints example , tieto type hints je the best 

def custom_addition(element1: int , element2: int) -> int:
    return element1 + element2
# ocakava element1 integer , element2 integer a vystup integer
# autor kodu presne povie co ocakava napr. od funkcie 
print(custom_addition(14, 5))

# ak chcete nieco zakomentovat alebo odkomentovat vo VS code stlacte skratku:
# ctrl + /
# takto viete zakomentovat aj viac oznacenych riadkov
