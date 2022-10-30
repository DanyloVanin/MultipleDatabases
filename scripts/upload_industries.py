import csv
import requests

db = 'neo4j_graph'
url = f'http://127.0.0.1:8000/{db}/industry'

# Industries
industries_file = open('resources/Industries.csv')
csvreader = csv.reader(industries_file)
total = 147
i=0
for industry in csvreader:
    i+=1
    industry_data = {'name': industry[0]}
    response = requests.post(url, json=industry_data)
    print(f'({i}/{total}) Company: {industry[0]} = {response.status_code}')
