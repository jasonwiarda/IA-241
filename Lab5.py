'''
lab 5 if statement
'''

#3.1
alien_color = 'red'

if alien_color == 'green':
    print('you just earned 5 points')
    
    
#3.2
alien_color = 'red'

if alien_color == 'green':
    print('you just earned 5 points')
    
else:
    print('you just earned 10 points')
    
#3.3

favorite_fruit = ['apple', 'orange', 'raspberry']

if 'orange' in favorite_fruit:
    print('You really like orange!')

if 'apple' in favorite_fruit:
    print('You really like apple!')

if 'raspberry' in favorite_fruit:
    print('You really like raspberry!')
    
#3.4

age = 23

if age < 10:
    print('You are a kid!')
elif age < 20:
    print('You are a teenager!')
else:
    print('You are an adult!')
    if age > 65:
        print('You are an elder!')
        