
def square_footage():
    area=[]
    print("First lets get the area\n")
    digits=input("What is your first digit")   
    area.append(digits)
    digits=input("What is your second digit")   
    area.append(digits)
    
    result=int(area[0])*int(area[1])

    print("The area of your room is "),
    print(result)
    print("\n")




def circm():
    print("Now lets get the circumference\n\n")
    r=float(input("Type your first digit\n"))
    result1=r*2
    result2=result1*(3.141592653589793)
    print("The circumference is aproximately ")
    print(result2)

