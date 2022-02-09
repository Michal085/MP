# Calculator
print("Vitajte v kalkulačke\n")
prvni_cislo = float(input("Zadajte prvé číslo: "))
druhe_cislo = float(input("Zadajte druhé číslo: "))
print("Súčet:", prvni_cislo + druhe_cislo)
print("Rozdiel:", prvni_cislo - druhe_cislo)
print("Súčin:", prvni_cislo * druhe_cislo)
print("Podiel:", prvni_cislo / druhe_cislo)
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
