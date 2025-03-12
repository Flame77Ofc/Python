# Cronômetro
import time
my_time = int(input('Enter with time seconds '))
for x in range(0, my_time):
    print(x)
    time.sleep(1)

# Timer:
my_time = int(input('Enter with time seconds '))
for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
