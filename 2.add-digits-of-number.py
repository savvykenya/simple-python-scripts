import sys
import math

#this function returns the sum of two digits. E.g. given 12, return 1+2=3. Given 145, returns 10.
def sum_of_digits(num):
    sumd=0
    while num>0:
        r=num%10
        sumd+=r
        num=math.floor(num/10)

    return sumd

if __name__ == "__main__":
    a = int(sys.argv[1])
    print(sum_of_digits(a))
    
