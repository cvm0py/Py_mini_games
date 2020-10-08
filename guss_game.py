import random
print("U will get 8 chances")
a = random.randint(1,1000)
i = 0
while i < 8:
    guess = int(input("Guess any number b/w 1 to 1000 : "))
    if guess!= a and i == 7 :
        print("U loose...")
        print("The ans is {}".format(a))
        break
    if guess > a:
        print("Plz guess lower")
        print()
    elif guess == a:
        print("U guessed it")
        print("u Guessed it in {} chances".format(i+1))
        break
    else:
        print("Plz guess Higher")
        print()
    i+= 1
    
