import colorama
from colorama import Fore, Style
import re, random
colorama.init()
dest = {
    'beaches': ['Maldives', 'Bora Bora', 'Bahamas', 'Phuket'],
    'mountains': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'],
    'cities': ['Paris', 'New York', 'Tokyo', 'London']
}
jokes = [
    'Why dont programmers like nature? It has too many bugs.',
    'Why did the computer go to the doctor? Because it had a virus!',
    'why do travelers always feel warm?, Because of their hot spots!'
]
def normalize_input(user_input):
    return re.sub(r"\s+", '', user_input).lower().strip()

def recommend():
    print(Fore.GREEN + 'TravelBot: Beaches, mountains, cities')
    preference = input('TravelBot: What type of destination do you prefer? '+ Style.RESET_ALL)
    preference = normalize_input(preference)
    if preference in dest:
        suggestion = random.choice(dest[preference])
        print(Fore.GREEN + 'How about?', suggestion)
        print('Do you like it? (yes/no)'+ Style.RESET_ALL)
        answer = input().lower().strip()
        if answer == 'yes':
            print(Fore.GREEN + f'Great! Have a wonderful trip to {suggestion}' + Style.RESET_ALL)
        else:
            print(Fore.GREEN + 'No worries! Feel free to ask for another recommendation.' + Style.RESET_ALL)
            recommend()
    else:
        print(Fore.GREEN + 'Sorry, I do not have recommendations for that type. Please choose from beaches, mountains, or cities.' + Style.RESET_ALL)
    show_help()
def tell_joke():
    joke = random.choice(jokes)
    print(Fore.YELLOW + 'Here is a joke for you:')
    print(joke + Style.RESET_ALL)
    show_help()
def show_help():
    print(Fore.CYAN + 'Type "recommend" for travel suggestions, "joke" for a travel joke, or "exit" to quit.' + Style.RESET_ALL)
def chat():
    print(Fore.CYAN + 'Welcome to TravelBot!')
    un = input('Please enter your name: ')
    print('Nice to meet you,', un + '!' + Style.RESET_ALL)
    show_help()
    while True:
        user_input = input('You: ')
        user_input = normalize_input(user_input)
        if user_input == 'exit':
            print(Fore.RED + 'TravelBot: Goodbye! Safe travels!' + Style.RESET_ALL)
            break
        elif user_input == 'recommend':
            recommend()
        elif user_input == 'joke':
            tell_joke()
        else:
            print(Fore.BLUE + 'TravelBot: I did not understand that command.' + Style.RESET_ALL)
            show_help()
if __name__ == '__main__':
    chat()