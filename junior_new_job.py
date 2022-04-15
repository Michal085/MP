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

#string_concatenation = "Hello" + " " +  "world" #ak chceme medzi Helloworld medzeru tak jednoducho + " " + cize vieme ich aj spajat
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
string_list = ["Michal", "Placko", "Joseph"]
combinated_list = [1, "Michal", "Joseph", True, 2.5]

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
#numbers + [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#numbers[0] = 10 # miesto 0 sa zmeni hodnota na 10 
#print(numbers)

# upravit vieme aj pomocou zloeneho indexu 
#numbers[1:3]
#numbers + [1, 2]
#print(numbers)

#Podmienky , CONDITIONS
# jednoducha podmienka . Splni sa ak je vyraz v podmienke pravda , vzdy musime cast vykonania oddelit  but tab alebo 4 medzerami
#is_student = True
#if is_student == True:
#    print("He is a programmer")

#is_programmer = True
#is_student = True
#if is_programmer ==False:
#    print("He is a programmer")
# ak vyraz nieje pravda tak python vykona kod v casti else
#else:
#    print("He is not a programmer")

# takto jednoducho vieme retazit podmienky ak neplati if python prejde na druhu elif a ak neplati ani ten prejde na else 
#if is_programmer == False:
#    print("Is not a programmer")
#elif is_student == True:
#    print("Is student")
#else:
#    print("Is programmer and is not a student")

# for cyklus
#numbers = [1, 2, 3, 4, 5, 6]
#for number in numbers:
# print(number)

#name = 'Michal'
#for character in name:
#   print(character)


#counter = range(0, 12)
#print(list(counter))

#def sucet_cisiel (cislo1, cislo2):
#    result = cislo1 + cislo2
#    return result

#x = (5 + 4) +3
#sucet = sucet_cisiel(cislo2=4, cislo1 =5)

# Dictionares - Slovniky
#my_dict = {
#   "key":"value",  # vzdy je na lavo kluc cize key a na pravo hodnota cize value 
#   "Michal": 31 ,
#   True: "True",
#   False: "True",
#}
#my_dict["Michal"] = 32  # zmena hodnoty pomocou kluca "Michal"
#print(my_dict["Michal"])

#person = { 
#    "name" : "Michal", 
#    "surname": "Placko", 
#    "languages": ["Python", "JavaScript", "Java"],
#    "instagram": "@misoplacko",
#    "address": {
#        "city": "New York",
#        "street": "stret_name",
#        "street_number": 45
#    }

#}
#print (person["languages"][-1])

#for kluc, hodnota in list(person.items()):
#   print("Key is: ", kluc)
#   print("Value is: ", hodnota)

#number_list = [1, 2, 3, 4, 8, 3, 29, 51, 79, 35, 78, 101, 114, 151, 156, 748, 14,]
#print(number_list[7])

# Tuple je to ako imutable list cize nemozme menit obsah 
# 
#first_tuple = 1, 2, 3, 4
#print(first_tuple)
#print(type(first_tuple))

#def function_returning_tuple(element1, element2):
#    return element1, element2

# x = function_returning_tuple("ahoj", "Michal")
#print(x)


# podtrznik znamena zamlcanie prvku 
# 3 ku nevypise
#x = (1, 2, 3)
#a,b,_ = x 
#print(a,b)
