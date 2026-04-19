import requests

def get_joke():
  url = 'https://official-joke-api.appspot.com/random_joke'
  response=requests.get(url)

  if response.status_code == 200:
    print(f'Full JSON Response: {response.json()}')
    data = response.json()
    return f'{data['setup']} - {data['punchline']}'

  else:
    return 'Something went wrong. Couldn\'t retrieve joke.'

def main():
  print('Welcome to the Random Joke Generator!')
  while True:
    user_input= input('Press enter to get a new joke, or type "q" / "exit" to quit: ').strip().lower()
    if user_input in ('q', 'exit'):
      print('Goodbye!')
      break

    joke = get_joke()
    print(joke)

if __name__ == '__main__':
  main()