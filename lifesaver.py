import collections
from gc import collect
import random

class LifeSaver:
    def __init__(self, flavor):
        self.flavor = flavor

tube= collections.deque()
flavors = ['orange','pineapple','cherry','raspberry','watermelon']
for l in range (1,10):
    flavor = flavors [random.randrange (0, len(flavors))]
    lifesaver = LifeSaver (flavor)
    tube.append (lifesaver)

while len(tube)>0:
    side= random.randrange (0,2)
    if side == 0:
        l =tube.pop()
        print ('Eating ' +l.flavor + ' from the right side')
    else: 
        l=tube.popleft()
        print ('Eating ' +l.flavor + ' from the left side')
print ('YUM!')


import collections
import random

class groceryline:
    def __init__(self, person):
        self.person = person

line= collections.deque()
people = ['Dave', 'Edith', 'Bob', 'Alice','Fred']
for l in range (1,101):
    people = people [random.randrange (0, len(people))]
    print ('adding ' + people +'to the line')
    line.append (groceryline (people))

if len (line) > 6:
    people = people [random.randrange (0, len (people))]
    print (people + 'left the line frustrated')
    line.append (groceryline(people))


stk1 = Stack ()
stk2 = Stack ()
stk3 = Stack ()

stk1.push ('big')
stk1.push ('medium')
stk1.push ('small')

print ('moving '+ stk1.top () + ' from stack 1 to stack 3')
disk = stk1.top ()
stk.pop()
stk3. push (disk)
print ('moving ' +stk1.top () + ' from stack 1 to stack 2')

