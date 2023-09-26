def notPoor(st):
  pnot = st.find('not')
  ppoor = st.find('poor')
  if ppoor > pnot and pnot>0 and ppoor>0:
    st = st.replace(st[pnot:(ppoor+4)], 'good')
    return st
  else:
    return st
print(notPoor(input()))
