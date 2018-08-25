from math import sqrt
_DEBUG = False
#        .
#       / \
#      / A \
#     /_____\
#    /   B   \
#   /_________\
#  /     C     \
# /_____________\
#

print("The segments dividing this triangle are parallel to the triangle's base.")
try:
    x = list(map(int, input("Height of different segments from top(input: spaced integers) ").split()))
except:
    print("Input Integers not something else")

solution_ratio = []
height_of_previous=0
for i in x:
    solution_ratio.append(((height_of_previous+i)**2)-(height_of_previous**2))
    height_of_previous +=i
if _DEBUG:
    print(solution_ratio)
print(str(solution_ratio.index(max(solution_ratio))+1)+" is the largest")
