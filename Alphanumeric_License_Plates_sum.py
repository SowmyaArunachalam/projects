def sumofno(n):
    sum2=0
    while(n!=0):
        q=n%10
        sum2+=q
        n//=10
    return sum2
    
l=input()
l1=l.split(" ")

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum1=0
s=0

for i  in l1:
    for j in i:
        if j.isalpha():
            sum1+=(alpha.index(j)+1)
            if sum1>9:
                sum1=sumofno(sum1)
        
for i  in l1:
    if i.isdigit():
        s+=sumofno(int(i))
        if s>9:
            s=sumofno(s)
    
res=s+sum1
if res>9:
    res=sumofno(res)
    
print(res)
