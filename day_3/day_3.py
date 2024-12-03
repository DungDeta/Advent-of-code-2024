import re
pattern = r"\(\d+,\d+\)"
input_file = open('input.txt', 'r')
lines = input_file.read()
print(lines)
def mul(x,y):
    return x*y
res=0
run=True
for i in range(len(lines)):
    if lines[i:i+4]=='do()':
        run=True
    if lines[i:i+7] == r"don't()":
        run=False
    if lines[i:i+3]=='mul' and run:
        print('found in index:',i)
        i=i+3
        nums=''
        while lines[i]!=')':
            nums+=lines[i]
            i+=1
        nums+=')'
        if re.match(pattern,nums):
            nums=nums[1:-1]
            nums=nums.split(',')
            res+=mul(int(nums[0]),int(nums[1]))
print(res)