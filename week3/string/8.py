def fll(st):
  try:
    if len(st) < 2 or st.isnumeric():
      raise Exception()
  except:
    print('Wrong input')
  else:
    return st[0:2] + st[-2:]
    
print(fll(input()))