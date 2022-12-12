def create_list(r1,r2):
    if (r1==r2):
        return r1
    else:
        res =[]
    while (r1<r2+1):
            res.append (r1)
            r1 +=1
    return res
r1, r2 = 1, 2022
for number in create_list(r1,r2):
    res = []
    if (number ** 408) % 2023 == 1:
        ans = []
        ans.append(number)
        print (ans)
    else:
        StopIteration    
