# Conditional Calculation Based om Number of Digits :

n= int(input("Enter any positive number: "))
if (n<0 or n>999):
    print("Invalid Number")
elif(n<10):
    print("The square of given number is :",n*n)
elif(n<100):
    print("The square root of given number is: ",n**0.5)
elif(n<1000):
    print("The cube root of given number is: ",n**(1/3))