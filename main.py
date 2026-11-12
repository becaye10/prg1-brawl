import random
import time

spelare_hp = 100

Spelare_namn = input("Vad heter du? ")

Fiende_val = input("Vill du möta Fiende 1 som är svag eller fiende 2 som är stark? ").lower

if Fiende_val == "fiende 2":
    fiende_hp = 150

if Fiende_val == "fiende 1":
    fiende_hp = 80
else:
    fiende_hp = 150

for countdown in range(1,4):
    time.sleep(0.5)
    print(countdown)

print(Spelare_namn ,"Hp =" ,spelare_hp ,"Fiende hp =", fiende_hp)

while True:
    spelare_hp -= random.randint(1,10)
    fiende_hp -= random.randint(1,10)
    print(Spelare_namn ,"Hp =" ,spelare_hp ,"Fiende hp =", fiende_hp)

    time.sleep(0.3)
    if spelare_hp <= 0:
        print("Fiende vann!")
        break
    elif fiende_hp <= 0:
        print(Spelare_namn,", Du vann!")
        break
    elif fiende_hp and spelare_hp<=0:
        print("Ingen vann")


