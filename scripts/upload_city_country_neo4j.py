import random

import requests
import csv

db = 'neo4j_graph'
country_url = f'http://127.0.0.1:8000/{db}/country'
city_url = f'http://127.0.0.1:8000/{db}/city'
world_cities = open('resources/world-cities.csv', encoding="utf8")
whitelist_countries = ['Ukraine', 'Germany', 'United Kingdom', 'Canada', 'Poland', 'United States']
cities_per_country = 5

csvreader = csv.reader(world_cities)
country_cities_dict = {}
for row in csvreader:
    if row[1] in country_cities_dict:
        country_cities_dict[row[1]].append(row[0])
    else:
        country_cities_dict[row[1]] = [row[0]]

i = 0
for country in whitelist_countries:
    i += 1
    cities_list = country_cities_dict[country]
    country_data = {'name': country}
    country_response = requests.post(country_url, json=country_data)
    if country_response.status_code == 409:
        continue
    country_response_json = country_response.json()
    print(f'({i}/{len(whitelist_countries)}) ==> Country: {country} - {country_response.status_code}')
    j = 0
    if len(cities_list) > cities_per_country:
        cities_list = random.choices(cities_list, k=cities_per_country)
    for city in cities_list:
        j += 1
        city_data = {'name': city, 'country': country}
        city_response = requests.post(city_url, json=city_data)
        print(f'({j}/{len(cities_list)}) City: {city} - {city_response.status_code}')
