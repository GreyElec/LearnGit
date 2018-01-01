# Exam4
list0=input()
list1=input()
if((len(list0))%8!=0):
    list0=list0+'0'*(8-(len(list0))%8)
Time0=int(len(list0)/8)
if((len(list1))%8!=0):
    list1=list1+'0'*(8-(len(list1))%8)
Time1=int(len(list1)/8)
def write(str):
    for i in range(int(len(str)/8)):
        print(str[i*8:(i+1)*8])
write(list0)
write(list1)
