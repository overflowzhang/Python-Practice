count = 0

def perm(n,begin,end):
    global count
    if begin >= end:
        print(n)
        count += 1
    else:
        i = begin
        for num in range(begin,end):
            n[num],n[i] = n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i] = n[i],n[num]

n = [1,2,3,4,5,6,7,8,9]
perm(n,0,len(n))
print(count)