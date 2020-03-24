#Surcharger les opérateurs : +, -, *, /, abs, == et != entre deux objets Complex (pour chaque opération, vérifier que le deuxième objet est une instance de la classe Cercle)


class Complex :
    def __init__(self,reel,ima):
        self.__reel=reel
        self.__imaginaire=ima

    def __add__(self,other):
        return Complex(self.__reel+other.__reel,self.__imaginaire+other.__imaginaire)
    def __sub__(self,other):
        return Complex(self.__reel-other.__reel,self.__imaginaire-other.__imaginaire)
    def __mul__(self,other):
        return Complex(self.__reel*other.__reel-self.__imaginaire*other.__imaginaire,self.__imaginaire*other.__reel+self.__reel*other.__imaginaire)
    def __truediv__(self,other):
        return Complex(self.__reel/other.__reel,self.__imaginaire/other.__imaginaire)

    def __eq__(self,other):
        return self.__reel==other.__reel and self.__imaginaire==other.__imaginaire
    def __ne__(self, other):
        return self.__reel!=other.__reel and self.__imaginaire!=other.__imaginaire
    def __abs__(self):
        return Complex(abs(self.__reel),abs(self.__imaginaire))
    def __str__(self):
        return 'cplx=('+str(self.__reel)+'+'+str(self.__imaginaire)+'i)'

if __name__ == '__main__' :
    c1=Complex(2,4)
    c2=Complex(3,6)
    c3=c1+c2
    c4=c1-c2
    c5=c1*c2
    c6=c1/c2
    c7=c1==c2
    c8=c1!=c2
    c9=Complex(-3,-5)
    c9=abs(c9)

    print(c3,c4,c5,c6,c7,c8,c9)


