class Duree :
    def __init__(self,heure,minute,seconde):
        self.__heure=heure
        self.__minute=minute
        self.__seconde=seconde

    def __add__(self, other):
        h=self.__heure+other.__heure
        m=self.__minute+other.__minute
        s=self.__seconde+other.__seconde
        while s>60 :
            m+=1
            s-=60
        while m>60 :
            h+=1
            m-=60
        return Duree(h,m,s)
    def __sub__(self, other):
        h=self.__heure-other.__heure
        m=self.__minute-other.__minute
        s=self.__seconde-other.__seconde
        while m<0 :
            h-=1
            m+=60
        while s<0 :
            m-=1
            s=s+60

        if h < 0 :
            return Duree(0,0,0)
        else :
            return Duree(h,m,s)
    def __str__(self):
        return str(self.__heure)+'h '+str(self.__minute)+'m '+str(self.__seconde)+str('s')

if __name__ == '__main__' :
    a=Duree(1,35,47)
    b=Duree(3,52,25)
    c=a+b
    print(c)
    c=a-b
    print(c)
    c=b-a
    print(c)
