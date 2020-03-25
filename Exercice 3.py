class Rational :
    def __init__(self,numerateur,denominateur):
        self.__numerateur=numerateur
        self.__denominateur=denominateur

    def __add__(self,other):
        return Rational(self.__numerateur*other.__denominateur+self.__denominateur*other.__numerateur,self.__denominateur*other.__ndeominateur)
    def __sub__(self,other):
        return Rational(self.__numerateur*other.__denominateur-self.__denominateur*other.__numerateur,self.__denominateur*other.__ndeominateur)
    def __mul__(self,other):
        return Rational(self.__numerateur*other.__numerateur,self.__denominateur*other.__denominateur)
    def __truediv__(self, other):
        return Rational(self.__numerateur*other.__denominateur,self.__denominateur*other.__numerateur)
    def __str__(self):
        return str(self.__numerateur)+'/'+str(self.__denominateur)



