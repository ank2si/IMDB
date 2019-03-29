straw = int(input())
side= straw/4    
remainder = straw%4
if remainder == 0:
    side1 =side
    side2 =side
elif remainder == 1:
    side1=side
    side2=side-1

product = side1*side2

print(product)