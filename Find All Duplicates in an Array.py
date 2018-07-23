### leetcode 442 medium

# on leetcode description there's a minor mistake about the complexity. since it's asking to return a list, 
# most of the answers that claim to have O(1) space are not actually in O(1) space. They are in O(n) space as the worse case
# is that the return list is the size of n/2. 

def findDuplicates(nums):
  output = []
  for n in nums:
    if nums[abs(n)-1] <0:
      output.append(abs(n))
    else:
      nums[abs(n)-1] *= -1 
  return output
# time complexity is O(n), n is the number of integers in the array.
