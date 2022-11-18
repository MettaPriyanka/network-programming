import pdb
def addition(a,b):
    answer=a + b
    return answer

pdb.set_trace()
x = int(input("enter the value1:"))
y = int(input("enter the value2:"))
sum = addition(x, y)
print(sum)