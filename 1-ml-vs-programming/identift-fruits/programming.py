
# This program follows the if else rules

def sort_fruits(color,shape):
    if color=="red" and shape=="round":
       return "Apple"
    elif color=="yellow" and shape=="long":
      return "Banana"
    else: 
       return "Unknown Fruit"

print(sort_fruits("red","round"))

print(sort_fruits("yellow","long"))
