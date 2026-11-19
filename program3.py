x=int(input("enter value 1:"))
y=int(input("enter value 2:"))
if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
else:
    print("Fourth Quadrant")