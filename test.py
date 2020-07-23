a = 5
b = 6
c = a+b
d = a**b
print(a,b,c,d)
print("%s %s %s %s" % (a,b,c,d))
print(a,"is a number")
print("%s is a number" % a)

num = 150
digit = 5
num_str = str(num)
digit_str = str(digit)
digit_is_in_number = digit_str in num_str
print(digit_is_in_number)

l = [1,2,3,4]
print(4 in l)

# comments
"""
like this
comments on multiple lines
"""

def add_a_and_b(a,b):
    return a+b

func = add_a_and_b(2,5)
print(func)

for i in range(10):
    print(i)

print()

for j in range(5,10):
    print(j)

x = True
y = False
if x is True:
    print("X is true")
if y is True:
    print("Y is true")
if x == False and y == False:
    print("Both false")
else:
    print("Both not false")

def print_odd(limit):
    for i in range(1,limit,2):
        print(i)

print_odd(10)

# list = []
# tuple = ()
# dictionary = {}

l1 = [1,5,10]
t1 = (1,5,10)
d1 = {
    "US" : "United States",
    "MX" : "Mexico",
    "CA" : "Canada"
}

print(d1["US"])
print(d1.keys())
print(d1.items())
print(d1.values())

