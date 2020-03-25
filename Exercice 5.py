import numpy as np

class Matrice :
    def __init__(self,mat):
        self.__matrice=mat

    def __add__(self,other):
        new_matrice=np.array([[0, 0],
                             [0,0]])
        for i in range (0,2) :
            for j in range (0,2) :
                new_matrice[i, j]= self.__matrice[i, j] + other.__matrice[i, j]

        return Matrice(new_matrice)

    def __sub__(self,other):
        new_matrice=np.array([[0, 0],
                             [0,0]])
        for i in range (0,2) :
            for j in range (0,2) :
                new_matrice[i, j]= self.__matrice[i, j] - other.__matrice[i, j]

        return Matrice(new_matrice)

    def __iadd__(self,other):

        for i in range (0,2) :
            for j in range (0,2) :
                self.__matrice[i, j] += other.__matrice[i, j]
        return self

    def __isub__(self,other):

        for i in range (0,2) :
            for j in range (0,2) :
                self.__matrice[i, j] -= other.__matrice[i, j]
        return self

    def __mul__(self,other):
        return Matrice(np.dot(self.__matrice,other.__matrice))
    def __imul__(self,other):
        self.__matrice=np.dot(self.__matrice,other.__matrice)
        return self

    def __str__(self):
        return str(self.__matrice)
    def __len__(self):
        return self.__matrice.shape()



if __name__ == '__main__' :
    a=np.array([[1,1],
               [1,1]])
    b=np.array([[1,0],
               [0,1]])
    a=Matrice(a)
    b=Matrice(b)
    c=a+b
    print(c)
    c=a-b
    print(c)
    a+=b
    print(a)
    a-=b
    print(a)
    c=a*b
    print(c)







