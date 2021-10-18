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
fprodlist=[0]
braclist=[]
rbraclist=[]
elementdict={}
val=""
mult=""
print(reac)
print(prod)
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
    k = 0
    h = 0
    for x in fprodlist:
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

            if fprodlist[k-1] != ")":
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
                    if fprodlist[p].isnumeric() == False and fprodlist[p] != ")" and fprodlist[p] != "(":
                        print("test")
                        if fprodlist[p].isupper() == True and fprodlist[p+1].isupper() == True:
                            print("good")
                            elementdict[fprodlist[p]] = elementdict[fprodlist[p]] * int(x)
                        if fprodlist[p+1].islower() == True and fprodlist[p].isupper() == True:
                            elementdict[fprodlist[p]+fprodlist[p+1]] = elementdict[fprodlist[p]+fprodlist[p+1]] * int(x)
                            print("yes")
                        if fprodlist[p].isupper() == True and fprodlist[p+1].isnumeric() == True:
                            print("ok")
                            elementdict[fprodlist[p]] = elementdict[fprodlist[p]] * int(x)
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

    
for i in range(len(reac)):
    print("i: ")
    print(i)
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
    print(elementlist)
    elementdict.clear()
    felementlist.clear()
    felementlist=[0]
print("yabadabadoooooo")
for i in range(len(prod)):
    for x in prod[i]:
        print(fprodlist)
        if str(fprodlist[-1]).isnumeric() and str(x).isnumeric():
            fprodlist[-1] = str(int(fprodlist[-1]) * 10 + int(x))
        else:
            if fprodlist[0] == 0:
                fprodlist[0] = x
            else:
                fprodlist.append(x)
            
    hashpr(prod[i])
    print(prod)
    prodlist.append(copy.deepcopy(elementdict))
    elementdict.clear()
    fprodlist.clear()
    fprodlist=[0]

print(elementlist)
print(prodlist)
