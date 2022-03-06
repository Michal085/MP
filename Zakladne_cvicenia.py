# Calculator
print("Vitajte v kalkulačke\n")
prvne_cislo = float(input("Zadajte prvé číslo: "))
druhe_cislo = float(input("Zadajte druhé číslo: "))
print("Súčet:", prvne_cislo + druhe_cislo)
print("Rozdiel:", prvne_cislo - druhe_cislo)
print("Súčin:", prvne_cislo * druhe_cislo)
print("Podiel:", prvne_cislo / druhe_cislo)
input("\nĎakujem za použitia kalkulačky, aplikáciu ukončíte ľubovoľnou klávesou.")

# Mocnina
a = int(input("Zadaj číslo k umocneniu: "))
vysledok = a * a
print("Výsledok:", vysledok)
input()

#Obvod a obsah kruhu
r = float(input("Zadaj polomer kruhu (cm): "))
o = 2 * 3.14 * r
s = 3.14 * r * r
print("Obvod zadaného kruhu je:", o, "cm")
print("Jeho obsah je", s, "cm^2")
input()

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)


#retazec = input('zadaj retazec: ')
#pocet = 0
#for znak in retazec:
#    pocet = pocet + 1      # alebo  pocet += 1
#print('dlzka retazca =', pocet)
#is_student = False
#is_programmer = True

#if is_programmer == False:
#    print("Is not a programmer")
#elif is_student == True:
#    print("Is student")
#else:
#    print("Is a programmer and is not a student")

#is_programmer = False
#if not is_programmer:
#    print("He is not a programmer")
#else:
#    print("He is a programmer")

#body = int(input('Zadaj pocet bodou'))
#if body >= 90:
# print('Za' , body , 'bodou ziskavas znamku A')
#else:
#    if body >= 80:
#        print('Za' , body , 'bodou ziskavas znamku B')
#    else:
#        if body >= 70:
#            print('Za' , body , 'bodou ziskavas znamku C')
#        else:
#                if body >= 60:
#                   print('Za' , body , 'bodou ziskava znamku D')
#              else:
#                    if body >= 50:
#                        print('Za' , body , 'bodou ziskavas znamku E')
#                    else:
#                        print('Za' , body , 'bodou si nevyhovel a ziskavas znamku FX')

# ZOZNAMY

#teploty = [6, 13, 28, 10, 17, 12, 24, 29]

sucet = sum(teploty) # ciselny sucet prvkov
maximum = max(teploty) # maximalny prvok hodnoty 
minimum = min(teploty)  # minimalny prvok hodnoty
priemer = sucet / len(teploty) #vrati pocet prvkou postupnosti
print(f'priemerna teplota je {priemer:.1f}')
print(f'minimalna teplota je {minimum}')
print(f'maximalna teplota je {maximum}')

ab = [2, 3, 5, 6, 9, 25]
ab[2] = 8
print(ab)

def sucet_cisiel(cislo1, cislo2):
   result = cislo1 + cislo2
   return result
sucet = sucet_cisiel(cislo2=5, cislo1=2)
sucet_cisiel(2, 5)
print('Sucet je' , sucet)

def string_addition_with_delimiter(string1, string2, delimiter ="**"):
    return string1 + delimiter + string2

temp = string_addition_with_delimiter("Michal", "Placko")
print(temp)

cisla = list(range(0,9))
print(cisla)

def sum_array(array):
    sucet = 0
    for number in array:
        sucet += number
        return sucet

print(sum_array(cisla))

def simple_sum(a, b):
    return  a + b

if simple_sum(4,3) > simple_sum(5, 2):
    print("First is bigger")
else:
    print("Second is bigger")

first_tuple = (1, 2, 3, )
print(first_tuple)

def sucet_cisiel(cislo1, cislo2):
    result = cislo1 + cislo2
    return result

x =(5 + 4) +3
sucet = sucet_cisiel(sucet_cisiel(cislo1=2 , cislo2=8),3)    
print(sucet)

cisla = list(range(0, 9))
print(cisla)

def sum_array(array):
    sucet = 0
    for number in array:
        sucet += number
    return sucet
print(sum_array(cisla))        

def sucet_cisiel(cislo1, cislo2):
    result = cislo1 + cislo2
    return result

x = (5 + 4) +3 
sucet = sucet_cisiel(sucet_cisiel(cislo2=10, cislo1=15),3)
print(sucet)

# Priemer
#pocet =0 
#suma = 0
#for cena in 1.75, 2.20, 1.03, 4.00, 3.50, 2.90, 1.89:
#    suma = suma + cena
#    pocet = pocet +1
#print("nakupil si", pocet ,"poloziek")
#print("Za", suma, "euro")
#print("Priemerna cena bola", round(suma/pocet, 2),"euro")

#strana = float(input('Zadaj stranu stvorca v centimetroch: '))
#cislo_je_spravne = strana > 0

#if cislo_je_spravne:
#    print('Obvod stvorca so stranou', strana, 'je', 4 * strana, 'cm')
#    print('Obsah stvorca so stranou', strana, 'je', strana * strana, 'cm2')
#else:
#    print('Strana musí byt kladná, inak z toho nebude stvorec!')

#print('Dakujeme za použití geometrickej kalkulačky.')
