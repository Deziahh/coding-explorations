
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

def analyze_sequence(n):
    collatz_seq = intGame(n)
    binary = intGameAi(n)
    
    ones_count = sum(binary)
    
    consecutive_distances = []
    last_index = -1
    for i, num in enumerate(binary):
        if num == 1:
            if last_index != -1:
                consecutive_distances.append(i - last_index)
            last_index = i
    
    avg_distance = sum(consecutive_distances) / len(consecutive_distances) if consecutive_distances else 0
    
    return ones_count, avg_distance

# Example usage:
initial_numbers = [7, 10, 15, 20]
for num in initial_numbers:
    ones_count, avg_distance = analyze_sequence(num)
    print(f"For initial number {num}:")
    print(f"Number of 1s: {ones_count}")
    print(f"Average distance between consecutive 1s: {avg_distance}")
    print()
