


Ques 1 
num = int(input(" Hey user , Enter a number "))
print(bin(num))



Ques 2 
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
        
        
        
 Ques 3 

Import math
n = int(input("Enter an integer"))
print((n+n*1)*(n+2))
print(n/2*(n-1))
r = int(input('enter radius'))
print(4*math.pi*r*r)
a = int(input('Enter angle 1:'))
b = int(input('Enter angle 1:'))
print(math.sqrt((r*math.cos(a)*2) + (r*math.sin(b)*2)))

x1 = int(input('Enter x coordinate of first point:'))
y1 = int(input('Enter y coordinate of first point:'))
x2 = int(input('Enter x coordinate of second point:'))
y2 = int(input('Enter y coordinate of second point:'))
print((y2-y1)/(x2-x1))



Ques 4 
print("First Part")
for i in range(5):
  print(i,"\n",end="")

print("Second Part")
for i in range(3,10):
  print(i,"\n",end="")

print("Third Part")
for i in range(4,13,3):
  print(i,"\n",end="")

print("Fourth Part")
for i in range(15,5,-2):
  print(i,"\n",end="")

print("Fifth Part")
for i in range(5,3):
  print(i,"\n",end="")
  
  
  
  
 Ques 5 
  
H = 1.00794
C = 12.0107
O = 15.9994
x = int(input("Enter the  number of Hydrogen atoms"))
y = int(input("Enter the  number of Carbon atoms"))
z = int(input("Enter the  number of Oxygen atoms"))
weight = x*H + y*C + z*O
print(weight)
