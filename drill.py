
# 1
a = 1
# 2
b = "string"
# 3
c = float(9.9)
# 4
print "2 minus 1 equals {}".format(a)
# 5
x = 10
y = 5

print   x + y
print   x - y
print   x * y
print   x / y
# add the 5 to the variable x and stores the result in x. x would become 15
x += 5
print   x
x -= 5
print   x
z = 2
print   y % z
# 6
t = True
f = False
print   (t and f)
print   (t or f)
print   (t and not f)
# 7
# none of the comparisons are True so prints "none are true"
# setting 5 in first statement or 15 in second will print "True"
# similerly, replacing (==) with (!=) will make the statements true.
if x - y != 10:
    print "True"
elif x + y == 10:
    print "True"
else:
    print "none are True"
# 8
# prints "y is not bigger than x" 5 until y becomes 11 which is bigger than x(10)
# so prints "y is now bigger than x"
def while_loop(x,y):
    stop = True
    while x > y:
        print "y is not bigger than x"
        y = (y + 1)
    stop = False
    print "y is now bigger than x"
while_loop(x,y)

#9
#prints 0-10
def for_loop():
    for f in range(11):
        print f
for_loop()
        
#10

MyList = [1,2,3,4,5]
for number in MyList:
    print (number)

#11

Tuple = (4,3,2,1,0)
for number in Tuple:
    print (number)

#12

def get_info():
    color = raw_input("What is your favorite color?: ")
    return color

#13
print get_info()










    



















