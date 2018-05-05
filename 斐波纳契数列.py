#斐波纳契数列,input term num
print("Type number")
first,second,op,t = 1,1,0,int(input())
while op < t:
    print(first)
    first,second=second,first+second
    op+=1
