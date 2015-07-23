'''
@author: Ashwin Gokhale
The sum of the reciprocals of squares from 1 to n is less than or equal to 2 - (1/n).

There are n people in a room and each person want to shake hands once with each other person in the room. How many handshakes occur?

Letting x = the square root of n, the sum of the reciprocals of positive square roots from 1 to n lies between x and (2x-1)

Prove that every third Fibonacci number is even.

Prove that each positive integer can be written as a sum of distinct Fibonacci numbers. (This question is a little harder.)

(If you like, you could try showing that the actual sum in the first exercise equals one sixth of the square of pi.) 
'''

from random import randint
from math import sqrt
#import math
def Induction1():
    print("-----------------------------------------------------------------------------------------")
    print("Induction 1:\nThe sum of the reciprocals of squares from 1 to n is less than or equal to 2 - (1/n): \n")
    randomNum = randint(1,100)
    # Initialize sum as 0 and compounded in for loop
    squareSum = 0
    
    # Compounds the sum
    for i in range(randomNum):
        # 1 / square of 1 - n
        squareSum += 1/(i + 1)**2
    
    RtSide = 2 - (1/randomNum)
    
    # 6 decimal places so you can see difference in answers
    RtSide = "%.6f" %RtSide
    squareSum = "%.6f" % squareSum
    print("Base:      " + str(squareSum) + " <= " + str(RtSide))
    
    # Copy and paste + 1
    randomNum2 = randomNum + 1
    squareSum2 = 0
    
    for i in range(randomNum2):
        squareSum2 += 1/(i + 1)**2
    
    RtSide2 = 2 - (1/randomNum2)
    RtSide2 = "%.6f" %RtSide2
    squareSum2 = "%.6f" % squareSum2
    print("Induction: " + str(squareSum2) + " <= " + str(RtSide2) + "\n")
    print("-----------------------------------------------------------------------------------------\n")

def Induction2():
    #n = int(input("How many people are in the room? (Please input an integer greater than 0):\n"))
    n = randint(1,100)
    # Formula is n(n-1)/2
    Handshakes = int((n*(n-1))/2)
    print("-----------------------------------------------------------------------------------------")
    print("Induction 2:\nThere are n people in a room and each person want to shake hands once with each other person in the room. How many handshakes occur?\n")
    print("Base:      If there were " + str(n) + " people in the room, " + str(Handshakes) + " handshakes occurred.")
    
    # Copy and paste + 1
    p = n + 1
    Handshakes2= int((p*(p-1))/2)
    print("Induction: If there were " + str(p) + " people in the room, " + str(Handshakes2) + " handshakes occurred.\n")
    print("-----------------------------------------------------------------------------------------\n")

def Induction3():
    print("-----------------------------------------------------------------------------------------")
    print("Induction 3:\nLetting x = the square root of n, the sum of the reciprocals of positive square roots from 1 to n lies between x and (2x-1)\n")
    randNum = randint(1,100)
    x = sqrt(randNum)
    # Initialize sum as 0 and compounded in for loop
    ssum = 0
    
    # Compounds the sum
    for i in range(randNum):
        ssum += 1/sqrt((i+1))
        
    LftSide = ((2*x)-1)
    
    # 2 decimal places so you can see difference in answers
    x = "%.2f"%x
    ssum = "%.2f" %ssum
    LftSide = "%.2f" %LftSide
    
    print("Base:      " + str(x) + " < " + str(ssum) + " < " + str(LftSide))
    
    # Copy and paste + 1
    randNum2 = randNum + 1
    x2 = sqrt(randNum2)
    # Initialize sum as 0 and compounded in for loop
    ssum2 = 0
    
    for i in range(randNum2):
        ssum2 += 1/sqrt((i+1))
        
    LftSide2 = ((2*x2)-1)
    
    # 2 decimal places so you can see difference in answers
    x2 = "%.2f" %x2
    ssum2 = "%.2f" %ssum2
    LftSide2 = "%.2f" %LftSide2
    
    print("Induction: " + str(x2) + " < " + str(ssum2) + " < " + str(LftSide2) + "\n")
    print("-----------------------------------------------------------------------------------------\n")
    
def Induction4():
    print("-----------------------------------------------------------------------------------------")
    print("Induction 4:\nProve that every third Fibonacci number is even.\n")
    # Formula for generating Fibonacci numbers
    # Adds next plus previous
    def fib(n):
        a = 0
        b = 1
        for i in range(0, n):
            temp = a
            a = b
            b = temp + b
        return a

    ranNum = randint(1,20)
    # Had to move up or would get ranNum*3 +1 *3
    ranNum2 = ranNum + 1
    
    ranNum = ranNum*3
    # Prints a random 3rd Fibonacci number
    print("Fibonacci Number:    " + str(ranNum))
    print("Base:                " + str(fib(ranNum)) + "\n")
    
    # Copy and paste + 1
    
    ranNum2 = ranNum2*3
    # Prints a random 3rd Fibonacci number
    print("Fibonacci Number:    " + str(ranNum2))
    print("Induction:           " + str(fib(ranNum2)) + "\n")
    print("-----------------------------------------------------------------------------------------\n")
    
    

def Induction5():
    print("-----------------------------------------------------------------------------------------")
    print("Induction 5:\nProve that each positive integer can be written as a sum of distinct Fibonacci numbers.\n")
    
    rNum = randint(1,1000)
    rNum2 = rNum + 1
    
    def z(n):
        a = 0
        b = 1
        fibNums = []
        rev = []
        for i in range(0, n):
            # Adds next plus previous
            temp = a
            a = b
            b = temp + a
            fibNums.append(a)
            
        # Reverses the Fibonacci numbers
        for i in reversed(fibNums):
            rev.append(i)
            
        print("The number:                                   "+ str(n))
        result = []
        ''' 
        Takes the random number(n) and subtracts it by the # of length of fibNums(f).
        Appends f to the result.
        Assigns n to be equal to n-f.
        Runs until n <= 0.
        '''
        while n > 0:
            for f in rev:
                if f <= n:
                    result.append(f)
                    n -= f
                    
        result.reverse()
        print("Can be represented as the Fibonnacci numbers: " + str(result).strip("[]") + "\n")
        print("-----------------------------------------------------------------------------------------\n")
    z(rNum)
    z(rNum2)

Induction1()
Induction2()
Induction3()
Induction4()
Induction5() 
