a = "bdd1a4e0b485f674748b275095cc8e7132beb37a1ae91db080abb2661e3badec"
b = "BDD1A4E0B485F674748B275095CC8E7132BEB37A1AE91DB080ABB2661E3BADEC"



for i in range(0,len(a)):
    if a[i] == b[i].lower():
        print("ok")
        pass

    else:
        print("not equal")
        break
