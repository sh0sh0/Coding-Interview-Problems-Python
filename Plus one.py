## EPI 5.2 Increment an arbitrary-precision integer
## Note: need to break from the loop if a digit is not 10, hence no need to carry-in a 1 for the next digit

def plusOne(A):
  A[-1] +=1
  for i in reserved(range(1, len(A))):
    if A[i] != 10:
      break
    A[i] = 0
    A[i-1] += 1
  if A[0] == 10:
    A[0] = 0
    A.insert(0, 1)
  return A
  
def main():
  A = [1,9]
  print(plusOne(A))

if __name__ == "__main__":
  main()
