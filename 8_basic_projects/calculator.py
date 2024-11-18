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

def choixdoperation(o, a, b):
    if o == 1:
        addition(a, b)
    elif o == 2:
        soustraction(a, b)
    elif o == 3 :
        multiplication(a, b)
    elif o == 4 :
        devision(a, b)
    elif o == 5:
        print("Au revoir !")
        return
    else :
        print("opperation introuvable")

print("--- Calculatrice ---")
print("chouisisser une opperation : ")
print(" 1 ) Addition \n 2 ) Soustraction \n 3 ) Multiplication \n 4 ) Division \n 5 ) Quitter")
print("choisisser l'opperation : ")
o = int(input())
print("opperateur 1 : ")
a = int(input())
print("opperateur 2 : ")
b = int(input())
choixdoperation(o ,a, b)