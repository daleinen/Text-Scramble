#-----------------------------------------------------
# a program that takes a string and randomly evolves into that text

import string
import random
import time

welcome = "\nWelcome to Text Evolver v1.0.0"
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

print(welcome)
target = input("\n\nEnter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))

completed = False
generation = 0
print()

while True:
    print(attemptThis)
    if attemptThis == target: break
    attemptNext = ''

    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
            
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.05)

print("\nTarget matched! That took " + str(generation) + " generation/s\n")
