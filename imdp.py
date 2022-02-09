import requests
from bs4 import BeautifulSoup
filmy_list = []
reziser_a_herci = []
r = requests . get('https://www.imdb.com/chart/top')
soup = BeautifulSoup(r.text, 'html.parser')
filmy = soup.find_all('td', class_='titleColumn')
for film in filmy:
    name = film.find_all('td' , class_='titleColumn')
    name = film.find('a').text
    year = film.find('span').text
    year_int = int(year.strip('()'))
    director_and_actors_list = film.find('a').get('title').split(',')
    director = director[0: -6]
    resault = [name, year, ]
    reziser_herci_=film.find('a').get('title')
    jmeno_rok_rez_herci = [name, year_int, reziser_a_herci]
    filmy_list.append(jmeno_rok_rez_herci)
    sorted_filmy = sorted(filmy_list, reverse=True, key=lambda x: x[1])
    print(sorted_filmy)

