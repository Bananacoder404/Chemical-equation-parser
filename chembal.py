import numpy as np

#determine reaction
print("Enter your reactants. An example of a correct entry is (Ag)(N)(O)3+(Cu).")
reac=input("REACTANTS: ")
print("Enter your products. An example of a correct entry is (Ag)+(Cu)((N)(O)3)2.")
prod=input("PRODUCTS: ")
reac = reac.replace(" ", "").split("+")
prod = prod.replace(" ", "").split("+")

reacn=[]
for i in range(len(reac)):
    for j in range(len(reac[i])):
        reacn.append(reac[i][j].replace(")", ""))

prodn=[]
for i in range(len(prod)):
    for j in range(len(prod[i])):
        prodn.append(prod[i][j].replace(")", " "))

print(reac)
print(reacn)

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
def getnumber(value):
    for character in value:
        if character.isdigit():
            return character
    return False


