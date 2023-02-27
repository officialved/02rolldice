import  random

ved = True
while ved :
    print(random.randint(1,6))
    vedant = input(" did you want to roll the dice 2nd time ?  y/n")
    if vedant.lower() == "y" :
        continue
    else:
        break
