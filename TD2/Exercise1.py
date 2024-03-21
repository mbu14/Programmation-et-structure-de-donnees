#Exercise1

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator==0:
            raise ValueError ("denominor must be nonzero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return '(%s/%s)'%(self.__numerator, self.__denominator)

    def __add__(self, other):
        self.__numerator=self.__numerator * other.__denominator + other.__numerator*self.__denominator
        self.__denominator= self.__denominator*other.__denominator
        return '(%s/%s)'%(self.__numerator,self.__denominator)

    def __mult__(self,other):
        self.__numerator=self.__numerator*other.__numerator 
        self.__denominator=self.__denominator*other.__denominator
        return '(%s/%s)'%(self.__numerator,self.__denominator)
    
    def __eq__(self, other):
        if self.__numerator==other.__denominator:
            return self.__denominator==other.__denominator
        return False
    
    def __pgcd__(self):
        if self.__numerator==0:
            return '(%s/%s)'%(other.__numerator,other.__denominator)
        r=self.__numerator%self.__denominator
        return __pgcd__(r)
    
if __name__=='__main__':

    fraction = Fraction(1,2)
    print(fraction) 

#Exercise2

