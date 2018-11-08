#EPI 5.3

def multiply(A,B):
  #step 1 store the sign
  sign = -1 if (A[0] < 0) ^ (B[0] < 0)  else 1
  A[0], B[0] = abs(A[0]), abs(B[0])
  
  #step 2 create result list
  result = [0]*(len(A) + len(B))
  
  #step 3 nested loops
  for i in reversed(range(len(A))):
      for j in reversed(range(len(B))):
          result[i + j + 1] += A[i] * B[j]
          result[i + j] += result[i + j + 1]//10
          result[i + j + 1] = result[i + j + 1] % 10
          
  #step 4 erase extra 0's in front
  num = 0
  while num < len(result) -1:
      if result[num] != 0:
          break
      num += 1
  result = result[num:]
  
  #step 5 add the sign
  return [result[0] * sign] + result[1:]
 
  
def main():
  A = [1,9,9]
  B = [-1]
  print(multiply(A,B))
  

if __name__ == "__main__":
  main()
