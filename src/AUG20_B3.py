from math import sqrt
_DEBUG = False

print("We have a rectangle inside a quater circle where two edges are on horizantal and vertical axis, one corner at center and other on the arc of quater circle")

x1 = float(input("Length left on vertical axis: "))
x2 = float(input("Length left on horizantal axis: "))

if x1>0 and x2>0:
    a = 1
    b = -2 * (x1+x2)
    c = (x1**2) + (x2**2)

    if _DEBUG:
        print(a, b, c)
    
    y1 = (-b+sqrt((b**2-(4*a*c))))/(2*a)
    y2 = (-b-sqrt((b**2-(4*a*c))))/(2*a)
    
    if _DEBUG:
        print(y1, y2)

    if y1>0 or y2>0:
        if y1>x1 and y1>x2:
            print("r= "+str(y1))
        if y2 > x1 and y2 > x2:
            print("r= "+str(y2))
    else:
        print("Given condition is not possible")
else:
    print("Input values greater than zero")
