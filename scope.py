factor = 10
n = 3

def verdubbel(getal):
    #global factor
    factor = 2
    print("Locals in func", locals())
    print("Globals in func", globals())
    #print("Voor", factor)
    print("Na", factor)
    return getal * factor

print(verdubbel(n))
print(factor)