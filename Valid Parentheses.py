### leetcode 20
### following code beats 99.87% python3 submissions as of august15,2018

  # because (, [, and { should be the first char we see in 
  # a valid parentheses pair, we put them in the values of 
  # the dictionary
  
def validP(s):
  stack = []
  dict = {")":"(","]":"[","}":"{"} 

  
  # when it's a first part of a parentheses, 
  # we need to save it in stack and later match 
  # with a proper second part which is a key in the dictionary
  
  for char in s:
    if char in dict.values():
      stack.append(char)
    elif char in dict.keys():
      if stack == [] or dict[char] != stack.pop():
        return False
    else:
      return False
  return stack == []
