def date_fashion(eu, par):
  if eu <= 2 or par <= 2:
    return 0
  if eu >= 8 or par >= 8:
    return 2
  return 1
