
def intGame(n):
    collatzSeq = []
    collatzSeq.append(n)
    while n != 1:
        if (n%2==0):
            n = n/2
            collatzSeq.append(int(n))
        else:
            n = 3*n+1
            collatzSeq.append(int(n))
    return collatzSeq

originalSeq = intGame(17)
print(originalSeq)

def intGameAi(n):
  binarySeq = []
  while n != 1:
      prev_n = n  
      n = n // 2 if n % 2 == 0 else 3 * n + 1

      binarySeq.append(1 if n > prev_n else 0)

  return binarySeq

binarySeq = intGameAi(17)
print(binarySeq)

