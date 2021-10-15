import copy
print("Enter your reactants. An example of a correct entry is (Ag)(N)(O)3+(Cu).")
reac=input("REACTANTS: ")
print("Enter your products. An example of a correct entry is (Ag)+(Cu)((N)(O)3)2.")
prod=input("PRODUCTS: ")
reac = reac.replace(" ", "").split("+")
prod = prod.replace(" ", "").split("+")


elementdict = {}
elementlist=[]
prodlist=[]
k=1
def hash(value):
    element = ""

    for x in value:
        if x.isupper():
                element = x
                elementdict[element] = 1
                element == ""
                element = x

        elif x.islower():
            elementdict.popitem()
            element = element+x
            elementdict[element] = 1

        elif x.isnumeric():
            elementdict[element] = int(x)

for i in range(len(reac)):
    print(reac[i])
    hash(reac[i])
    elementlist.append(copy.deepcopy(elementdict))
    elementdict.clear()

for j in range(len(prod)):
    print(prod[j])
    hash(prod[j])
    prodlist.append(copy.deepcopy(elementdict))
    elementdict.clear()

print(elementdict)
print(elementlist)
print(prodlist)
print(prod)
print(reac)

