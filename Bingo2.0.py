#Bingo2.0

def isEqual(a,b):
    if a<b:
        print ("too small!")
        return False

    elif a>b:
        print ("too big!")
        return False

    else :
        print ("Bingo!")
        return True

loop = True

while loop == True:
    
    print ("Guess what I think?(1-100)")
    bingo = False
    from random import randint
    num = randint(1,100)
    
    
    while bingo == False:
        answer = int(input())
        bingo = isEqual(answer,num)
    
    while bingo == True:
        print ("Do you want to try again? (type 1 = yes other numbers = no)")
        want = int(input())
        if want == (1):
            bingo = False
            loop = True

        else:
            loop = False
            print ("Thanks! Game over!")
            bingo = False
