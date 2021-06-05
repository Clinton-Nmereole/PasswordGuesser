import numpy as np
import random as rand
alphabets = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                        'r','s','t','u','v','w','x','y','z'])
passlength = int(input("Enter password length: "))
password = input("Enter the password: ")
guesspass = ""
tries = 0
with open("mydictionary.txt") as file:
    contents = file.read()
    if password in contents:
        guesspass = password
        print("The password is "+ guesspass + " it was found in the dictionary.")
    else:
        while guesspass != password :
            guess = rand.choices(alphabets, k = passlength)
            guesspass = "".join(guess)
            tries += 1
print(f'it took {tries} tries to find the password, and the password is {guesspass}')
