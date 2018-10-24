temp1=input()
temp2=input()
i=0
k=0
temp1=temp1.casefold()
temp2=temp2.casefold()
j=temp1.find(temp2,i)
for each in temp1:
    if(j>=0):
        i=j+1
        k+=1
        j=temp1.find(temp2,i)
print(k)
       
