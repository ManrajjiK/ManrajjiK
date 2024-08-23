#string :data type that stores seqence of characters
str1=" this is manraj "
str2='welcome to jec jabapur '
str3= """DEPATMENT OF MECHATRONICS ENGINEERING"""


#concatination
print(str1+str2+str3)
print(len(str1), len(str2), len(str3))
print(str1[3])

#slicing

print(str1[1:5])
print(str1[:5])
print(str1[5:])
print(str2[-5:-3])

#fuction
str='sir i am a coder'

print(str.endswith("er"))
print(str.capitalize())
print(str.replace("o", "r"))
print(str.find("r"))
print(str.count("am"))

#conditional statements

#if-elif-else statements

light="green"
if(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Slow down")
elif(light=="green"):
    print("go") 
else :
    print("light is broken")


marks=87  

if(marks>=90 ):
    print("marks A")
elif(70<=marks <80) :
    print("marks B")
elif(60<=marks <70):
    print("grade C")
elif(50<=marks < 60):
    print("grade D") 
else :
    print("grade E")       


#Nesting  
# Get input from the user
number=8

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")



    # Get three numbers from the user
num1 = 78
num2 = 8
num3 = 5

# Find the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
# Print the result
print(f"The greatest of the three numbers is: {greatest}")





# Get input from the user
number = 78

# Check if the number is a multiple of 7
if number % 7 == 0:
    print(f"{number} is a multiple of 7.")
else:
    print(f"{number} is not a multiple of 7.")




    
       