from requests import get
from bs4 import BeautifulSoup

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = 'python'

response = get(f'{base_url}{search_term}')

if 200 != response.status_code:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find_all('section', class_='jobs'))


def say_hello(name, age):
    print(f'Hello {name}, you are {age} years old')


say_hello('John', 30)
