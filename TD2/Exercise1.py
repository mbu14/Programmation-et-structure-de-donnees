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
        if self.__numerator==0:
            return '(%s/%s)'%(other.__numerator,other.__denominator)
        r=self.__numerator%self.__denominator
        return __pgcd__(r)
    
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

#Exercise2

