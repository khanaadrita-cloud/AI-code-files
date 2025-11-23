import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()
print(Fore.CYAN + 'Welcome to sentiment analysis app!' + Style.RESET_ALL)
un = input('Please enter your name: ')
if not un:
    un = 'Mystery Agent'

cl = []
print(Fore.YELLOW + 'Hello ' + un + Style.RESET_ALL)
print('Enter the sentence, and i will analyse the sentiment using TextBlob.')
print('Type "exit" to quit, "reset" to clear, "history" to view past analyses.')

while True:
    user_input = input('Enter your answer: ')
    if not user_input:
        print('Enter a valid sentence.')
        continue
    if user_input == 'exit':
        print('Goodbye!')
        break
    elif user_input == 'reset':
        cl.clear()
        print('History cleared.')
        continue
    elif user_input == 'history':
        if not cl:
            print('No history available.')
        else:
            print('History of analysis is:')
            for v in cl:
                print(v)
        continue

    p = TextBlob(user_input).sentiment.polarity
    if p > 0:
        sentiment = 'Positive'
    elif p < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    result = 'sentiment: '+ sentiment + ', polarity: '+ str(p)
    print(result)
    cl.append(result)