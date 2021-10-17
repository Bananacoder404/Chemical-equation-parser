import copy
import sympy as sp
print("Enter your reactants. An example of a correct entry is Ag(NO)3+Cu.")
reac=input("REACTANTS: ")
print("Enter your products. An example of a correct entry is Ag+Cu(NO3)2.")
prod=input("PRODUCTS: ")
reac = reac.replace(" ", "").split("+")
prod = prod.replace(" ", "").split("+")
print(reac)

elementlist=[]
prodlist=[]
felementlist=[0]
fprodlist=[]
braclist=[]
rbraclist=[]
elementdict={}
val=""
mult=""

def hashel(value):
    element = ""
    k = 0
    h = 0
    for x in felementlist:
        x = str(x)
        print(elementdict)
        if x.isupper():
            element = x
            elementdict[element] = 1
            element == ""
            element = x
            k = k+1
            h = h+1

        elif x.islower():
            elementdict.popitem()
            element = element+x
            elementdict[element] = 1
            k = k+1
            h = h+1

        elif x.isnumeric():

            if felementlist[k-1] != ")":
                elementdict[element] = int(x)
                k = k+1
                h = h+1
                
            else:
                cordfirst = braclist[-1]+1
                cordlast = rbraclist[0]
                braclist.pop()
                rbraclist.pop(0)
                print(cordfirst)
                print(cordlast)
                for p in range(cordfirst, cordlast):
                    print("super")
                    if felementlist[p].isnumeric() == False and felementlist[p] != ")" and felementlist[p] != "(":
                        print("test")
                        if felementlist[p].isupper() == True and felementlist[p+1].isupper() == True:
                            print("good")
                            elementdict[felementlist[p]] = elementdict[felementlist[p]] * int(x)
                        if felementlist[p+1].islower() == True and felementlist[p].isupper() == True:
                            elementdict[felementlist[p]+felementlist[p+1]] = elementdict[felementlist[p]+felementlist[p+1]] * int(x)
                            print("yes")
                        if felementlist[p].isupper() == True and felementlist[p+1].isnumeric() == True:
                            print("ok")
                            elementdict[felementlist[p]] = elementdict[felementlist[p]] * int(x)
                k = k+1
                h = h+1
                print("confirmation")

        elif x == "(":
            braclist.append(k)
            k = k+1
            h = h+1
            
        elif x == ")":
            rbraclist.append(h)
            k = k+1
            h = h+1
                
#H(NO3)2(Pb(ClK3)5)2+H2O
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
                print(braclist)
                k = k+1
for i in range(len(reac)):
    for x in reac[i]:
        if str(felementlist[-1]).isnumeric() and str(x).isnumeric():
            felementlist[-1] = str(int(felementlist[-1]) * 10 + int(x))
        else:
            if felementlist[0] == 0:
                felementlist[0] = x
            else:
                felementlist.append(x)
    print(felementlist)

    hashel(reac[i])
    print(elementdict)
    print(elementlist)
    elementlist.append(copy.deepcopy(elementdict))
    elementdict.clear()
    felementlist.clear()
    felementlist=[0]

    for i in range(len(prod)):
        hashpr(prod[i])
        prodlist.append(copy.deepcopy(elementdict))
        elementdict.clear()
        fprodlist.clear()
        fprodlist=[0]

print(elementlist)
print(prodlist)
