#Exercise1

class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return '(%s/%s)'%(self.__numerator, self.__denominator)


if __name__=='__main__':

    fraction = Fraction(1,2)
    print(fraction) 
