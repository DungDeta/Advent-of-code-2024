input_file = open('input.txt', 'r')
lines = input_file.readlines()
arr_1=[]
arr_2=[]
for line in lines:
    num=line.split('   ')
    arr_1.append(int(num[0]))
    arr_2.append(int(num[1]))
arr_1=sorted(arr_1)
arr_2=sorted(arr_2)
res=0
distance=0
for i in range(len(arr_1)):
    distance=abs(arr_1[i]-arr_2[i])
    res+=distance
print(res)