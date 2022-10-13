"""ADD SUBTRACT MULTIPLY DIVIDE
    -IF OPERATIONS"""

oper= float(input("Select operator: \n 1 -> +\n 2 -> -\n 3 -> *\n 4 -> / "))

if oper == 1:
    nr1= float(input("Please give first number: "))
    nr2= float(input("Please give second number: "))
    print("RESULT: " + str(nr1 + nr2))
elif oper == 2:
    nr1= int(input("Please give first number: "))
    nr2= int(input("Please give second number: "))
    print("RESULT: " + str(nr1 - nr2))
elif oper == 3:
    nr1= int(input("Please give first number: "))
    nr2= int(input("Please give second number: "))
    print("RESULT: " + str(nr1 * nr2))
elif oper == 4:
    nr1= int(input("Please give first number: "))
    nr2= int(input("Please give second number: "))
    print("RESULT: " + str(nr1 / nr2))
else :
    print("please give valid operator!")    

