import random

stay =0
switch =0

for i in range(1000):
    door=[1,0,0]
    random.shuffle(door)
    choice=random.randrange(3)
    user=door[choice]
    del(door[choice])
    door.remove(0)
    if user==1:
        stay+=1
    if door[0]==1:
        switch+=1

print("Win on Staying:",stay/1000)
print("Win on Switching:",switch/1000)
