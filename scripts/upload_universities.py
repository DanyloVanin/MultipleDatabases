import csv
import random

db = 'postgresql'
url = f'http://127.0.0.1:8000/{db}/education'
total = 500

# Universities
universities_file = open('resources/world-universities.csv', encoding="utf8")
csvreader = csv.reader(universities_file)
universities = []
for row in csvreader:
    universities.append(row[1])

random_universities = random.choices(universities, k=3)
i=0
print(random_universities)
# for university in random_universities:
#     i+=1
#     university_data = {'name': university[1]}
#     # response = requests.post(url, json=university_data)
#     print(f'({i}/{total}) University: {university[3]} = {response.status_code}')
