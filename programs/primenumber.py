def prime_(num):
    count=0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count==2:
        return "Prime Number"
    else:
        return "Not a Prime Number"

#num=int(input("Enter any num: "))
#print(prime_(num))
