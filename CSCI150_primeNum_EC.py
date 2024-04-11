def primeNumbers(n):
    allNum = [2, 3, 5, 7]
    for i in range(3,n+1):
        if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0: 
            continue
        else:
            allNum.append(i)
         
    return allNum

a = primeNumbers(101)
print(a)