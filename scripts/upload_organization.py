import csv
import requests

db = 'neo4j_graph'
url = f'http://127.0.0.1:8000/{db}/organization'

csv_file = open('resources/constituents_csv.csv')
csvreader = csv.reader(csv_file)
total = 505
i=0
for company in csvreader:
    i+=1
    data = {'name': company[1]}
    response = requests.post(url, json=data)
    print(f'({i}/{total}) Organization: {company[1]} = {response.status_code}')
