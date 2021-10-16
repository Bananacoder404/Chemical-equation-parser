import copy
import sympy as sp
print("Enter your reactants. An example of a correct entry is Ag(NO)3+Cu.")
reac=input("REACTANTS: ")
print("Enter your products. An example of a correct entry is Ag+Cu(NO3)2.")
prod=input("PRODUCTS: ")
reac = reac.replace(" ", "").split("+")
prod = prod.replace(" ", "").split("+")


elementlist=[]
prodlist=[]
felementlist=[]
fprodlist=[]
braclist=[]
elementdict={}
val=""
mult=""

def hashel(value):
    element = ""
    for i in range(len(value)):
        k = 0
        for x in value[i]:
            felementlist.append(x)

            if x.isupper():
                element = x
                elementdict[element] = 1
                element == ""
                element = x
                k = k+1

            elif x.islower():
                elementdict.popitem()
                element = element+x
                elementdict[element] = 1
                k = k+1

            elif x.isnumeric():
                if felementlist[felementlist.index(x)-1] != ")":
                    elementdict[element] = int(x)
                    k = k+1
                else:
                    cordfirst = braclist[-1]+1
                    cordlast = felementlist.index(x)-1
                    braclist.pop()
                    for i in range(cordfirst, cordlast):
                        if felementlist[i].isnumeric() == False and felementlist[i] != ")" and felementlist[i] != "(":
                            elementdict[felementlist[i]] = elementdict[felementlist[i]] * int(x)
            
                    k = k+1

            elif x == "(":
                braclist.append(k)
                k = k+1

def hashpr(value):
    element = ""
    for i in range(len(value)):
        k = 0
        for x in value[i]:
            fprodlist.append(x)

            if x.isupper():
                element = x
                elementdict[element] = 1
                element == ""
                element = x
                k = k+1

            elif x.islower():
                elementdict.popitem()
                element = element+x
                elementdict[element] = 1
                k = k+1

            elif x.isnumeric():
                if fprodlist[fprodlist.index(x)-1] != ")":
                    elementdict[element] = int(x)
                    k = k+1
                else:
                    cordfirst = braclist[-1]+1
                    cordlast = fprodlist.index(x)-1
                    braclist.pop()
                    for i in range(cordfirst, cordlast):
                        if fprodlist[i].isnumeric() == False and fprodlist[i] != ")" and fprodlist[i] != "(":
                            elementdict[fprodlist[i]] = elementdict[fprodlist[i]] * int(x)
            
                    k = k+1

            elif x == "(":
                braclist.append(k)
                k = k+1

for i in range(len(reac)):
    print(reac[i])
    hashel(reac[i])
    elementlist.append(copy.deepcopy(elementdict))
    elementdict.clear()
    braclist.clear()
    felementlist.clear()

for i in range(len(prod)):
    print(prod[i])
    hashpr(prod[i])
    prodlist.append(copy.deepcopy(elementdict))
    elementdict.clear()
    braclist.clear()
    fprodlist.clear()

print(elementlist)
print(prodlist)
