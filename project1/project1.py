print('Hello, I am AI chat bot. What is your name?')
name = input()
print(f'Nice to meet you, {name}.')

print('How are you feeling today?')
feeling = input('Enter "good" or "bad": ')
if feeling.lower() == 'good':
    print(f'That\'s great, {name}!')
elif feeling.lower() == 'bad':
    print(f'I hope you feel better soon, {name}.')
else:
    print('I\'m not sure what that means, but I hope you have a good day!')

print('How old are you?')
age = input()
print(f'Wow, {age} years old! That\'s a great age to be.')

print('What is your favorite color?')
color = input()
print(f'{color} is a beautiful color!')

print('what are your hobbies?')
hobbies = input()
print(f'{hobbies} sound like fun!')

print('whats your favourite subject in school?')
subject = input()
print(f'{subject} is an interesting subject!')

print('whats your favorite food?')
food = input()
print(f'{food} sounds delicious!')

print('what do you want to be when you grow up?')
career = input()
print(f'Becoming a {career} sounds exciting!')

print(f'It was nice talking to you, {name}. Goodbye!')

