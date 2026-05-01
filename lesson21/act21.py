import requests

url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en'

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f'Did you know? {fact_data['text']}')
    else:
        print('Failed to retrieve text.')

while True:
    fact = input('Press enter for a random technology fact or press q to quit: ')
    if fact.lower() == 'q':
        print('goodbye!')
        break

    get_random_technology_fact()