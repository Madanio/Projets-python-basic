# this is the project one 
def addition(a,b) : 
    x = a + b
    print ("le resultat de l'opperation et : ")
    print(f" {a} + {b} = {x}")

def soustraction(a,b) : 
    x = a - b
    print ("le resultat de l'opperation et : ")
    print(f" {a} - {b} = {x}")

def multiplication(a,b) : 
    x = a * b
    print ("le resultat de l'opperation et : ")
    print(f" {a} x {b} = {x}")

def devision(a,b) : 
    if b == 0 : 
        print("Error : devision par zero ")
    else :
        x = a / b
        print ("le resultat de l'opperation et : ")
        print(f" {a} / {b} = {x}")