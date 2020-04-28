def firstDuplicate(a):
  b=set()
  for num in a:
    if num in b:
      return num
    b.add(num)
  return -1
