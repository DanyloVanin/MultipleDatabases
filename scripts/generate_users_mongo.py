import requests
from faker import Faker
import random
import csv
from faker.providers import internet
from faker.providers import job

db = 'mongo'
url = f'http://127.0.0.1:8000/{db}'
NUM_USERS = 1000
QUERY_LIMIT = 500

fake = Faker()
fake.add_provider(internet)
fake.add_provider(job)

# Get industries
industries = []
industries_file = open('resources/Industries.csv')
csvreader = csv.reader(industries_file)
for industry in csvreader:
    industries.append((industry[0]))

# Get languages
languages = []
languages_file = open('resources/Languages.csv', encoding="utf8")
csvreader = csv.reader(languages_file)
for lang in csvreader:
    languages.append((lang[3]))

# Get cities
country_cities = []
world_cities = open('resources/world-cities.csv', encoding="utf8")
whitelist_countries = ['Ukraine', 'Germany', 'United Kingdom', 'Canada', 'Poland', 'United States']
cities_per_country = 50
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
    j = 0
    if len(cities_list) > cities_per_country:
        cities_list = random.choices(cities_list, k=cities_per_country)
    for city in cities_list:
        j += 1
        data = {'city': city, "country": country}
        country_cities.append(data)


# Get organizations
organizations = []
csv_file = open('resources/constituents_csv.csv')
csvreader = csv.reader(csv_file)
for company in csvreader:
    organizations.append(company[1])

# Get universities
universities_file = open('resources/world-universities.csv', encoding="utf8")
csvreader = csv.reader(universities_file)
universities = []
for row in csvreader:
    universities.append(row[1])

# Get contact types
contact_types = ['Twitter', 'Instagram', 'Email', 'TikTok', 'LinkedIn', 'GitHub']

# Create user
for _ in range(NUM_USERS):
    industry = random.choice(industries)
    country_city = random.choice(country_cities)
    languages = list(set(random.choices(languages, k=random.choice(range(1, 4)))))

    # Create fake contacts
    num_contacts = random.randrange(1, 4)
    i = 0
    contacts = []
    while i < num_contacts:
        i += 1
        contact_url = fake.url()
        contact_type = random.choice(contact_types)
        contact_data = {'type': contact_type, 'url': contact_url}
        print(contact_data)
        contacts.append(contact_data)

    # Create fake education
    education = []
    num_education = random.randrange(1, 3)
    i = 0
    while i < num_education:
        i += 1
        university_name = random.choice(universities)
        year_start = random.randrange(1970, 2015)
        year_end = year_start + random.choice([4, 6])
        education_data = {'school_name': university_name, 'year_start': year_start,
                          'year_end': year_end}
        print(education_data)
        education.append(education_data)

    # Create fake work experience
    num_work_experience = random.randrange(1, 5)
    i = 0
    work_experience = []
    while i < num_work_experience:
        i += 1
        job_title = fake.job()
        year_start = random.randrange(1970, 2015)
        year_end = year_start + random.randrange(1, 15)
        organization = random.choice(organizations)
        work_experience_data = {'job_title': job_title, 'year_start': year_start,
                                'year_end': year_end, 'organization': organization}
        print(work_experience_data)
        work_experience.append(work_experience_data)

    fullname = fake.name()
    firstname = fullname.split()[0]
    lastname = fullname.split()[1]
    user_data = {'first_name': firstname, 'last_name': lastname, 'industry': industry, 'city': country_city['city'],
                 'country': country_city['country'],
                 'languages': languages, "contacts": contacts, "education": education,
                 "work_experience": work_experience}
    print(user_data)
    response = requests.post(url + '/user', json=user_data).json()
