# 1
hodnoty = [44,54,64,74,104]
plus_sest = [x+6 for x in hodnoty]
print(plus_sest)

2
cars_kilos ={"Sedan": 1500, "Kodiaq": 2000, "Pickup": 2500, "Man": 16000, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
cars_names_up_to_2500 = [car for car in cars_kils if cars_kilos[car]<2500]
print(cars_names_up_to_2500)
3
akcie = ["META", "GOOG", "AMZN", "NTFX", "AAPL"]
cena = [100, 130, 160, 299, 120]
akcie_cena = {stock:price for stock, price in zip(akcie, cena)}
print(akcie_cena)

import requests
import csv
from bs4 import BeautifulSoup
def filmy_list():
 text = ""
r = requests.get("https://www.cas.sk/clanok/2616795/koronavirus-nadalej-drzi-slovensko-v-pazuroch-vysoky-narast-nakazenych-i-obeti/")
soup = BeautifulSoup(r.text, "html.parser")
text_field = soup.find("div", {"id" : "introtext mt20"})
print(text_field)

strana = float(input('Zadaj stranu stvorca v centimetroch: '))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod stvorca so stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah stvorca so stranou', strana, 'je', strana * strana, 'cm2')
else:
    print('Strana musí byt kladná, inak z toho nebude stvorec!')

print('Dakujeme za použitie geometrickej kalkulačky.')




