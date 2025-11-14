print('Hello, i am AI chat bot. whats your name?')
name = input()
print('nice to meet you', name)
print('how are you feeling today?')
feeling = input('enter as good or bad: ')
if feeling == 'good':
    print('thats great', name)
elif feeling == 'bad':
    print('I hope you feel better soon,', name)
else:
    print('invalid input')

print('It was nice talking to you,', name)