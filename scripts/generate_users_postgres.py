import requests
from faker import Faker
import random
import csv
from faker.providers import internet
from faker.providers import job

db = 'postgresql'
url = f'http://127.0.0.1:8000/{db}'
NUM_USERS = 200
QUERY_LIMIT = 500

fake = Faker()
fake.add_provider(internet)
fake.add_provider(job)

# Get industries
params = {'limit': QUERY_LIMIT}
industries = requests.get(url + '/industry', params=params).json()
industry_ids = list(map(lambda x: x['id'], industries))

# Get languages
params = {'limit': QUERY_LIMIT}
languages = requests.get(url + '/language', params=params).json()
language_ids = list(map(lambda x: x['id'], languages))

# Get cities
params = {'limit': QUERY_LIMIT}
cities = requests.get(url + '/city', params=params).json()
city_ids = list(map(lambda x: x['id'], cities))

# Get organizations
params = {'limit': QUERY_LIMIT}
organizations = requests.get(url + '/organization', params=params).json()
organization_ids = list(map(lambda x: x['id'], organizations))

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
    industry_id = random.choice(industry_ids)
    city_id = random.choice(city_ids)
    lang_ids = list(set(random.choices(language_ids, k=random.choice(range(1, 4)))))

    fullname = fake.name()
    firstname = fullname.split()[0]
    lastname = fullname.split()[1]
    user_data = {'first_name': firstname, 'last_name': lastname, 'industry_id': industry_id, 'city_id': city_id,
                 'language_ids': lang_ids}
    print(user_data)
    response = requests.post(url+'/user', json=user_data).json()
    print(user_data)
    user_id = response['id']

    # Create fake contacts
    num_contacts = random.randrange(1, 4)
    i = 0
    while i < num_contacts:
        i += 1
        contact_url = fake.url()
        contact_type = random.choice(contact_types)
        contact_data = {'user_id': user_id, 'type': contact_type, 'url': contact_url}
        print(contact_data)
        requests.post(url + '/contact', json=contact_data)

    # Create fake education
    num_education = random.randrange(1, 3)
    i = 0
    while i < num_education:
        i += 1
        university_name = random.choice(universities)
        year_start = random.randrange(1970, 2015)
        year_end = year_start + random.choice([4, 6])
        education_data = {'user_id': user_id, 'school_name': university_name, 'year_start': year_start,
                          'year_end': year_end}
        print(education_data)
        requests.post(url + '/education', json=education_data)

    # Create fake work experience
    num_work_experience = random.randrange(1, 5)
    i = 0
    while i < num_work_experience:
        i += 1
        job_title = fake.job()
        year_start = random.randrange(1970, 2015)
        year_end = year_start + random.randrange(1, 15)
        organization_id = random.choice(organization_ids)
        work_experience_data = {'user_id': user_id, 'job_title': job_title, 'year_start': year_start,
                                'year_end': year_end, 'organization_id': organization_id}
        print(work_experience_data)
        requests.post(url + '/work-experience', json=work_experience_data)