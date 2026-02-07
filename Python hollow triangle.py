a=int(input("Enter the no.of rows:"))
#THE LEFT ANGLE HOLLOW TRIANGLE

for i in range(1,a+1):
    print()
    for j in  range(1,a+1):
        if j==1 or i==a or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")

#THE LEFT ANGLE (RIGHT ALIGEMNET) HOLLOW TRIANGLE
"""
for i in range(1,a+1):
    print()
    for j in range(1,a+1):
        if i==a or j==a or  j==a-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
"""

#THE INVERSE LEFT ANGLE HOLLOW TRIANGLE
"""
for i in range(1,a+1):
    print()
    for j in  range(1,a+1):
        if i==1 or j==a or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
 """

#THE INVERSE LEFT ANGLE (RIGHT ALIGEMNET) HOLLOW TRIANGLE
"""
for i in range(1,a+1):
    print()
    for j in  range(1,a+1):
        if i==1 or j==1 or j==a-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
            """