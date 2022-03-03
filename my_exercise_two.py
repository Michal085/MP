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

#sucet = sum(teploty) # ciselny sucet prvkov
#maximum = max(teploty) # maximalny prvok hodnoty 
#minimum = min(teploty)  # minimalny prvok hodnoty
#priemer = sucet / len(teploty) #vrati pocet prvkou postupnosti
#print(f'priemerna teplota je {priemer:.1f}')
#print(f'minimalna teplota je {minimum}')
#print(f'maximalna teplota je {maximum}')

ab = [2, 3, 5, 6, 9, 25]
ab[2] = 8
print(ab)