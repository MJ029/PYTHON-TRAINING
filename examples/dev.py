#Different Types of Creating Integers [maximum ways]
#Single Variable
a=100
print(a)
#Multiple Variable

#method 1
a=100
b=32
print(a,b)

#method 2
a,b = 12,34
print(a,b)

#From list
a = [21,324,5467,6,36,35,32]
print(a[4])
#From Tuple
a = (21,324,5467,6,36,35,32)
print(a[2])

#Swapping

#Swap 2 integers
a=12
b=43
a,b = b,a
print(a,b)

#Swap 3 Integers

def swapThree(a, b, c):

    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)
    print("After swapping a =", a, ", b =", b, ", c =", c)

if __name__ == '__main__':
    a = 10
    b = 20
    c = 30
    print("Before swapping a =", a, ", b =", b, ", c =", c)
    swapThree(a, b, c)

# Duplicate Given Integer "19930622"
a=19930622
print((str(a)+' ') * 3)

#Integer Reverse
num =19930622
print(str(num)[::-1])

#Convert list of integers to integers
a = [9, 6, 8, 8, 5, 1, 4, 4, 4, 3]
for i in a:
    print(i, end="")
print("")

#Sort Integer
a=[0,9,8,7,6,1,2,3,4,5]
a.sort()
print(a)

#spliting integers

a=[9688514443]
b= list(map(int, str(a[0])))
print(b)