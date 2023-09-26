def ingOrLy(st):
  l = len(st)
  if l >= 2:
    if st[-3:] == 'ing':
      st += 'ly'
    else:
      st += 'ing'
    return st
#print(ingOrLy(input()))

def cc(st):
  try:
    if len(st) < 2 or not(st.isalpha()):
      raise Exception()
  except:
    print("Wrong input")
  else:
    if st[-3:] == 'ing':
      st += 'ly'
    else:
      st += 'ing'
    print(st)
cc(input())