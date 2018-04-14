from random import randint

num = randint(1,100)

bingo = False

while bingo == False:
    print ("What is the number?(The number is between 1 and 100.)")
    ans = int(input())

    if ans>num:
        print ("No...%d is too big!"%ans)

    if ans<num:
        print ("No...%d is too small!"%ans)

    if ans==num:
        print ("Bingo! %d is the correct answer!"%ans)

    if ans==num:
        bingo = True
