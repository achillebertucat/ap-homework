

filename = 'dossiernoms.txt'

def parsing(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            content= line.split(' ')
            dictio = {'firstname' : content[0], 'lastname' : content[1], 'date' : content[2] + ' ' + content[3] + ' ' + content[4] }
            result.append(dictio)
    return(print(result))

#on supprime les sauts de ligne dans le dossier du prof
import time
start = time.time()

set_first= set()
set_last= set()

with open('first_names.txt') as first:
    for line in first:
        set_first.add(str(line.rstrip()))

with open('last_names.txt') as last:
    for line in last:
        set_last.add(str(line.rstrip()))

import random
people = set()
new_set = set()

while len(people)<1000:
    print('B')
    random_name = str(random.choices(set_first, k=1) + ' ' + random.choices(set_last, k=1))
    random_birthday = str(random.randint(1,29) + '/' + random.randint(1,12) +'/' + random.randint(2000,2004))
    print('A')
    if random_name not in people:
        people.add(random_name)
        new_set.add(random_name + ' ' + random_birthday)

with open('data-big.txt', 'w') as data:
    for element in new_set:
        data.write( element + '\n')

end = time.time()
lenght = end - start
print('le temps dexecution est de ' + lenght + 'secondes')

