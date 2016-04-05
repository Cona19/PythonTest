import math
import random
from audioop import mul

'''
a = int(raw_input('a>>'))
b = int(raw_input('b>>'))
c = int(raw_input('c>>'))

t = math.sqrt(b*b -4 * a * c)
result1 = (-b + t) / (2 * a)
result2 = (-b - t) / (2 * a)

print str(result1) + ", " + str(result2)
'''
'''
n = int(raw_input("n="))

i = 1
while i < 10:
    print str(n) + " x " + str(i) + " = " + str(n*i)
    i += 1

'''
'''
n = int(raw_input("n="))

i = 1
while i <= n:
    print " "*(n-i) + "*"*(i*2-1)
    i += 1
'''

'''
n = int(raw_input('n='))

for i in range(1,10):
    print "%d x %d = %d" % (n, i, n * i)
'''
'''
toInt = {'Rock': 0, 'Scissors': 1, 'Paper': 2}
result = {0:{0:0, 1:1, 2:-1},1:{0:-1, 1:0, 2:1},2:{0:1, 1:-1, 2:0}}
desc = {0: "Draw", 1:"Win", 2:"Lose"}
score = 0

while score < 3:
    mystr = raw_input("Your Rock / Scissors / Paper = ")
    userOut = toInt.get(mystr, "None")
    comOut = random.randint(0, 2)

    print desc[result[userOut][comOut]]
    score += result[userOut][comOut]
'''
'''
mylist = [1,2,3,4,5,6]
print [x**2 for x in mylist if (x%2) == 0]

mylist2 = []
for i in mylist:
    if i % 2 == 0:
        mylist2.append(i**2)

print mylist2

print [x for x in range(0,5) if ( x % 2 == 1)]
'''

'''
users = {1:2, 2:3, 3:4, 4:{'a':'b', 'b':'c'}, 5:(1,4,3,2)}
for key in users.keys():
    print key, users[key]

for key, value in users.iteritems():
    print key, value
    '''
'''
def quadratic_formula(a, b, c):
    d = math.sqrt(b**2 - 4 * a * c)
    if d > 0:
        return ()
    elif d == 0:
        return ((-b + d)/(2 * a),)
    else:
        return ((-b + d)/(2 * a), (-b - d)/(2 * a))

print quadratic_formula(1,2,1)

def test(a):
    a.append(1)
    return a

x = [2]
test(x)
print x
'''

multiply_add = lambda a, b, c : (a+b) * c

print multiply_add(1,2,3)