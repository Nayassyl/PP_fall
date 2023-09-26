def f2l3(st):
  if len(st) < 2:
    return st *  2

  return st[0:2] + st[-2:]

#print(f2l3(input()))

# def fll(st):
#     try: 
#     except :
#         print('Not a string')
#     else:
#         if len(st) < 3:
#             return st *  2
#     finally:
#         return st[0:2] + st[-2:]

# print(fll(input()))

def fll(st):
  try:
    if len(st) < 2 or not(st.isalpha()):
      raise Exception()
  except:
    print('Wrong input')
  else:
    return st[0:2] + st[-2:]
    
print(fll(input()))