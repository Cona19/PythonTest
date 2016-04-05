import math
a = int(raw_input('a>>'))
b = int(raw_input('b>>'))
c = int(raw_input('c>>'))

t = math.sqrt(b*b -4 * a * c)
result1 = (-b + t) / (2 * a)
result2 = (-b - t) / (2 * a)

print str(result1) + ", " + str(result2)
