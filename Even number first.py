## from EPI book, chapter 5
## given a list of integers, return the list with even numbers appear first
## you can create a new list, which will require extra space
## you can also using two pointers, one for even (starts from the beginning), and one for odd (starts from the end), to 
## the list into three parts: even, unclassified, odd

def evenFirst(A):
  even, odd = 0, len(A) - 1
  while even < odd:
    if A[even] % 2 == 0:
      even += 1
    else:
      A[even], A[odd] = A[odd], A[even]
      odd -= 1
  return A
  
