class Rational :
    def __init__(self,numerateur,denominateur):
        self.__numerateur=numerateur
        self.__denominateur=denominateur

    def __euclide(self,a,b):
        while a != b :
            if a>b :
                a-=b
            else :
                b-=a
        return a


    def __add__(self,other):
        if isinstance(other,Rational) :
            return Rational(self.__numerateur*other.__denominateur+self.__denominateur*other.__numerateur,self.__denominateur*other.__denominateur)
    def __sub__(self,other):
        if isinstance(other,Rational) :
            return Rational(self.__numerateur*other.__denominateur-self.__denominateur*other.__numerateur,self.__denominateur*other.__denominateur)
    def __mul__(self,other):
        if isinstance(other,Rational) :
            return Rational(self.__numerateur*other.__numerateur,self.__denominateur*other.__denominateur)
    def __truediv__(self, other):
        if isinstance(other,Rational) :
            return Rational(self.__numerateur*other.__denominateur,self.__denominateur*other.__numerateur)
    def __str__(self):
            return str(self.__numerateur)+'/'+str(self.__denominateur)
    def __eq__(self,other):
        a=self.__euclide(other.__numerateur,other.__denominateur)
        print(a)
        New_other=Rational(other.__numerateur/a,other.__denominateur/a)
        a=self.__euclide(self.__numerateur,self.__denominateur)
        print(a)
        New_self=Rational(self.__numerateur/a,self.__denominateur/a)
        return New_other.__numerateur == New_self.__numerateur  and  New_other.__denominateur == New_self.__denominateur







if __name__ == '__main__' :
    a=Rational(1,2)
    b=Rational(2,4)
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print(a==b)
    print(type(a))
    print(c,d,e,f)



