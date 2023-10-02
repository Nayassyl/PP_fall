def enc(a):
    res = ''
    for i in range(0, len(a), 2): res += a[i]
    for i in range(1, len(a), 2): res += a[i]
    return res
def dec(a):
    len=len(a)
    half_length=(len+1)//2
    even=a[:half_length]
    odd=a[half_length:]
    res=''
    if len%2==0:
        for i in range (half_length):
            join=even[i]+odd[i]
            res += join
    else:
        for i in range (1,half_length+1):
            start=i-1
            join=even[start:i]+odd[start:i]
            res += join
    return res

print(enc(input()))
print(dec(input()))
