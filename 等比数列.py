#等比数列

loop = 1

while loop == 1:
    print("type a value")
    value = int(input())
    for i in range(0,10):
        ans = value**i
        print (ans)
    print ("again? 1=yes")
    loop = int(input())
    if loop != 1:
        print ("thnaks!")

    
