# The conditionals and the booleans values

def check_weather():
    weather = 'rain'
    if weather == 'rain':
        print('☔')
    else:
        print('😎')
    print(weather)

def greet_friend():
    friend = True
    if friend:
        print('Hello, friend!')
    else:
        print('Hi')

def check_my_points():
    my_points = 36
    if my_points > 30:
        print('I win!')
    else:
        print('Oh no, I lose.')

def check_team_points():
    team_points = 176
    if team_points > 200:
        print('Yeee, we win!')
    else:
        print('Good luck next time!')

def greeting(greet, name):
    print(f"{greet}, {name}")

def sum(a, b):
    print(a + b)


check_weather()
greet_friend()
check_my_points()
check_team_points()
greeting('Hello', 'Gabriel')
sum(6, 7)