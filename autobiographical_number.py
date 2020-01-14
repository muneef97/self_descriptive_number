def self(digit):
    start = pow(10,digit-1)
    end = (digit-1)*start
    check = 0
    for i in range(start,end):
        count = []
        for k in range(digit):
            count.append(0)
        for j in str(i):
            if(int(j)<digit):
                count[int(j)]+=1
        c = 0
        temp = 0
        for j in str(i):
            if( int(j) == count[c]):
                temp += 1
            c+=1
        if(temp==digit):
            check += 1
            print(str(i))
    if(check==0):
        print("not found")
    return temp

digit = int(input("Enter the digit : "))
self(digit)

