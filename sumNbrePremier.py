#   somme des n nombres premiers :
def nombrePremierEntreUnEtN():
    n = int(input("Donnez un entier :\t\n"))
    for j in range(n):
        res=0
        test=0
        for i in range(1,j+1):
            if j%i==0:
                test=test+1
        if test==2:
            res=res+i
    print("res=",res)
if __name__ == '__main__':
    nombrePremierEntreUnEtN()
