#Exercise1&2

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator==0:
            raise ValueError ("denominator must be nonzero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return '(%s/%s)'%(self.__numerator, self.__denominator)

    def __add__(self, other):
        new_numerator=self.__numerator * other.__denominator + other.__numerator*self.__denominator
        new_denominator= self.__denominator*other.__denominator
        return '(%s/%s)'%(new_numerator,new_denominator)

    def __mult__(self,other):
        new_numerator=self.__numerator*other.__numerator 
        new_denominator=self.__denominator*other.__denominator
        return '(%s/%s)'%(new_numerator,new_denominator)
    
    def __eq__(self, other):
        if self.__numerator==other.__denominator:
            return self.__denominator==other.__denominator
        return False
    
    def __pgcd__(self):
        a=self.__numerator
        b=self.__denominator
        if self.__numerator==0:
            return '(%s/%s)'%(self.__numerator,otselfher.__denominator)
        while b:
            a, b = b, a % b
        return a
    
    def __simplify__(self):
        diviseur= self.__pgcd__()
        new_numerator= self.__numerator/diviseur
        new_denominator= self.__denominator/diviseur
        return '(%s/%s)'%(new_numerator,new_denominator)
    
    def __suite_harmonique__(self=1, n=10000):
        somme=self
        for i in range (2,n+1):
            somme = somme.__add__(somme)
        return somme.__simplify__()
    
if __name__=='__main__':

    #test1 - test fraction
    fraction = Fraction(1,2)
    print(fraction) 
    
    #test2- test addition
    fraction1= Fraction(3,4)
    fraction2= Fraction(1,2)
    sum_fraction= fraction1.__add__(fraction2)
    print ("Addition :", sum_fraction)

    #test3 - test multiplication
    mult_fraction= fraction1.__mult__(fraction2)
    print ("Multiplication :", mult_fraction)

    #test4 - test pgcd
    fraction3 = Fraction(8,10)
    simplified = fraction3.__simplify__()
    print("simplify fraction : ", simplified)

    #test5 - suite harmonique
    result= __suite_harmonique__()
    print(result)
#Exercise3

