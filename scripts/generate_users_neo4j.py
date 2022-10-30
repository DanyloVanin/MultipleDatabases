import requests
from faker import Faker
import random
import csv
from faker.providers import internet
from faker.providers import job

db = 'neo4j_graph'
url = f'http://127.0.0.1:8000/{db}'
NUM_USERS = 250
QUERY_LIMIT = 500

fake = Faker()
fake.add_provider(internet)
fake.add_provider(job)

# Get industries=
industries = requests.get(url + '/industry').json()
industries = list(map(lambda x: x['name'], industries))

# Get languages=
languages = requests.get(url + '/language').json()
languages = list(map(lambda x: x['name'], languages))

# Get cities
cities = requests.get(url + '/city').json()
cities = list(map(lambda x: x['name'], cities))

# Get organizations
organizations = requests.get(url + '/organization').json()
organizations = list(map(lambda x: x['name'], organizations))

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
    city = random.choice(cities)
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
    user_data = {'first_name': firstname, 'last_name': lastname, 'industry': industry, 'city': city,
                 'languages': languages, "contacts": contacts, "education": education,
                 "work_experience": work_experience}
    print(user_data)
    response = requests.post(url + '/user', json=user_data).json()
