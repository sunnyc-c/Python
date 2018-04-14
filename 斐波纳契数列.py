#斐波纳契数列
loop = 1
while loop == 1:
    print("Type")

    value = int(input())
    a = 1
    b = 1

    for i in range (0,value):
        if i < 2:
            print("1")
        elif i %2 != 0:
            a += b
            print(a)
        else:
            b += a
            print (b)

    print ("Retry? 1=yes")
    loop = int(input())

    if loop != 1:
        print("Thanks!")
