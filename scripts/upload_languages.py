import csv
import requests

db = 'neo4j_graph'
url = f'http://127.0.0.1:8000/{db}/language'

# Languages
languages_file = open('resources/Languages.csv', encoding="utf8")
csvreader = csv.reader(languages_file)
total = 185
i = 0

for language in csvreader:
    i += 1
    language_data = {'name': language[3].strip()}
    response = requests.post(url, json=language_data)
    print(f'({i}/{total}) Language: {language[3]} = {response.status_code}')
