import colorama
from colorama import Fore, Style
import re, random
from datetime import datetime

import pytz  # Install with: pip install pytz

colorama.init()

dest = {
    'beaches': ['Maldives', 'Bora Bora', 'Bahamas', 'Phuket'],
    'mountains': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'],
    'cities': ['Paris', 'New York', 'Tokyo', 'London']
}

jokes = [
    'Why dont programmers like nature? It has too many bugs.',
    'Why did the computer go to the doctor? Because it had a virus!',
    'Why do travelers always feel warm? Because of their hot spots!',
    'Why did the scarecrow become a successful traveler? Because he was outstanding in his field!'
]

# Timezone mapping for destinations
place_to_timezone = {
    'india': 'Indian/Maldives',
    'bora bora': 'Pacific/Tahiti',
    'bahamas': 'America/Nassau',
    'phuket': 'Asia/Bangkok',
    'swiss alps': 'Europe/Zurich',
    'rocky mountains': 'America/Denver',
    'himalayas': 'Asia/Kathmandu',
    'paris': 'Europe/Paris',
    'new york': 'America/New_York',
    'tokyo': 'Asia/Tokyo',
    'london': 'Europe/London'
}

def normalize_input(user_input):
    return re.sub(r"\s+", '', user_input).lower().strip()

def get_time(place):
    """Get current time in specified place"""
    normalized_place = normalize_input(place)
    timezone_str = place_to_timezone.get(normalized_place)
    
    if not timezone_str:
        return f"Sorry, I don't know the timezone for '{place}'. Try: Maldives, Paris, Tokyo, etc."
    
    try:
        tz = pytz.timezone(timezone_str)
        current_time = datetime.now(tz)
        time_str = current_time.strftime("%A, %B %d, %Y at %I:%M %p (%Z)")
        return f"The current time in {place.title()} is: {time_str}"
    except Exception:
        return f"Could not get time for {place}. Please check the spelling."

def recommend():
    print(Fore.GREEN + 'TravelBot: Beaches, mountains, cities')
    preference = input('TravelBot: What type of destination do you prefer? '+ Style.RESET_ALL)
    preference = normalize_input(preference)
    if preference in dest:
        suggestion = random.choice(dest[preference])
        print(Fore.GREEN + f'How about {suggestion}?'+ Style.RESET_ALL)
        print('Do you like it? (yes/no)')
        answer = input().lower().strip()
        if answer == 'yes':
            print(Fore.GREEN + f'Great! Have a wonderful trip to {suggestion}!'+ Style.RESET_ALL)
            # Show current time in destination
            time_info = get_time(suggestion)
            print(Fore.CYAN + time_info + Style.RESET_ALL)
            print('Would you like some packing tips? (yes/no)' + Style.RESET_ALL)
            tips_answer = input().lower().strip()
            if tips_answer == 'yes':
                if preference == 'beaches':
                    print(Fore.GREEN + 'Packing tips: Sunscreen, swimwear, sunglasses, flip-flops.' + Style.RESET_ALL)
                elif preference == 'mountains':
                    print(Fore.GREEN + 'Packing tips: Warm clothing, hiking boots, rain jacket, backpack.' + Style.RESET_ALL)
                elif preference == 'cities':
                    print(Fore.GREEN + 'Packing tips: Comfortable walking shoes, city map, camera, light clothing.' + Style.RESET_ALL)
        else:
            print(Fore.GREEN + 'No worries, here\'s another recommendation:' + Style.RESET_ALL)
            print(Fore.GREEN + f'How about {suggestion}?'+ Style.RESET_ALL)
        print('Do you like it? (yes/no)')
        answer = input().lower().strip()
    else:
        print(Fore.GREEN + 'Sorry, I do not have recommendations for that type. Please choose from beaches, mountains, or cities.' + Style.RESET_ALL)
    show_help()

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.YELLOW + 'Here is a joke for you:')
    print(joke + Style.RESET_ALL)

def show_help():
    print(Fore.CYAN + 'Type "recommend" for travel suggestions, "joke" for a travel joke, "time [place]" for current time, or "exit" to quit.' + Style.RESET_ALL)

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
        elif user_input.startswith('time'):
            # Extract place after "time"
            place_input = user_input.replace('time', '', 1).strip()
            if place_input:
                time_info = get_time(place_input)
                print(Fore.LIGHTMAGENTA_EX + time_info + Style.RESET_ALL)
                show_help()
            else:
                print(Fore.RED + 'Please specify a place: "time Paris"' + Style.RESET_ALL)
        else:
            print(Fore.BLUE + 'TravelBot: I did not understand that command.' + Style.RESET_ALL)
            show_help()

if __name__ == '__main__':
    chat()
