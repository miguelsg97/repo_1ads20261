def sum13(nums):
  soma = 0
  for i in nums:
    if i == 13:
        break
    soma += i
  return soma