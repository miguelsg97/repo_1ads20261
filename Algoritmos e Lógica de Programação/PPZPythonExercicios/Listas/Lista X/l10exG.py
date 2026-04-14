def count_code(s):
  k = 0
  for i in range(len(s) - 3):
    if s[i] == 'c' and s[i+1] == 'o' and s[i+3] == 'e':
      k += 1
  return k