# EPI 5.4
# Goal: reach the end position of the array, i.e. len(A)-1
# condition: max steps <= A[i]
# use while loop for advancing
# when we go through the list, we keep track of the furthest position we can reach
# if at the end, we can reach the last position or more than it's True, otherwise False

def reach_end(A):
  furthest, last_position = 0, len(A) -1
  i = 0
  while i <= furthest and furthest <= last_position:
    furthest = max(furthest, A[i]+i)
    i +=1
  return furthest >= last_position
