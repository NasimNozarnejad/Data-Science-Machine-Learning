import random
import numpy as np
NUM=1000
Bob_wins=0
Doors=[1, 2, 3]
Bob_chance=0
for i in range(1,NUM+1):
    Car=np.random.randint(1,3)
    Bob_choice=np.random.choice(Doors)
    if Bob_choice == Car:
        Bob_wins+=1
        Bob_chance=Bob_wins/i       
        
NUM=1000
Alice_wins=0
Alice_chance=0
for i in range(1,NUM+1):
    Car=np.random.randint(1,3)
    Doors=[1, 2, 3]
    Doors.remove(Car)
    Sheep=Doors
    Doors=[1, 2, 3]
    Alice_choice=np.random.choice(Doors)
    if Alice_choice != Car:
        Sheep.remove(Alice_choice)
        Opened_door=int(Sheep[0])
    else:
        Opened_door=np.random.choice(Sheep)
    
    Doors.remove(Alice_choice)
    Doors.remove(Opened_door)
    Alice_new_choice=Doors
    if int(Alice_new_choice[0]) == Car:
        Alice_wins+=1
        Alice_chance=Alice_wins/i

print('Alice\'s chance of winning is: ' + str(Alice_chance))
print('Bob\'s chance of winning is: ' + str(Bob_chance))
