def bilgiVer(ad, soyad="Girilmedi", yas="Girilmedi"):
    return f"Ad:{ad}, Soy ad:{soyad}, Yaş:{yas}"


# print(bilgiVer("Ali", 34))


def bilgiVer2(ad, soyad="Girilmedi", yas="Girilmedi"):
    return f"Ad:{ad}, Soyad:{soyad}, Yaş:{yas}"


# print(bilgiVer2("Ali", yas=34))
# print(bilgiVer2())
# print(bilgiVer2("Çalışkan",yas=23))

def topla2 (x,y):
    return x + y

def topla3 (x,y,z):
    return x+y+z

def topla(*args):
    for arg in args:
        print(arg)

# topla(1,2,3,4,5,"Python",True)

def carp(*args):
    carpim=1
    for arg in args:
        carpim*=arg
    return carpim

def ortalama(*args):
    return sum(args)/len(args)

# print(ortalama(5,8,10,17))

def fonk(**kwargs):
    print(kwargs)
# fonk(ad="Ali",soyad="Çalışkan",yaş=34)

def fonk2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("***************")
    for arg in  args:
        print(arg)
    print("**********************")
    for kwarg in kwargs:
        print(kwarg)

fonk2(2,33,4,5,7,8,ad="ali", yas=23)