# fibonacci series

nterms=int(input("enter a number: "))
a=0
b=1
sum=a+b
count=3
if nterms<=0:
    print("enter a number greater than zero")

elif 1>=nterms>0:
    print(a)

elif 2>=nterms>0:
    print(a)
    print(b)

elif nterms>2:
    print(a)
    print(b)
    while count<=nterms:
        print(sum)
        count=count+1
        a=b
        b=sum
        sum=a+b  
