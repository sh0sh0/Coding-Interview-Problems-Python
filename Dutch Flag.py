## EPI 5.1 
## break the array into three parts: less than pivot (les), equal to (eq), and greater than (gr). 
## time complexity is O(n), n is the number of integers in A
## space complexity is O(1) 

def dutchFlag(pivot_ind, A):
  pivot = A[pivot_ind]
  les, eq, gr = 0, 0, len(A)-1
  while les < gr:
    if A[eq] < pivot:
      A[eq], A[les] = A[les], A[eq]
      les += 1
      eq +=1
    elif A[eq] == pivot:
      eq += 1
    else:
      A[eq], A[gr] = A[gr], A[eq]
      gr -= 1
  return A
  
def main():
  pivot_ind = 1
  A = [0, 1, 0, 0, 2]
  print(dutchFlag(pivot_ind, A))

if __name__ == "__main__":
  main()
      
