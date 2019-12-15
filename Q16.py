
'''
Q16. Write a program that requests a positive four-digit integer from the user and prints its digits. You are not allowed to 

use the string data type operations to do this task. Your program should simply read the input as an integer and 

process it as an integer, using standard arithmetic operations (+, *, -, /, %, etc).

Test Data:

Enter n: 1234

Expected Output:

1

2

3

4
'''
#Solution0
n = int(input("n: "))
d = int(n % 10)
c = int(((n % 100) )/10)
b = int(((n % 1000) )/100)
a = int(((n% 10000))/1000)
print(a, b, c ,d, sep = "\n")
print()

#Solution1
n = int(input("n: "))
a = (int(n/1000))
b = int(n/100) - (10*a)
c = int(n/10)  - (100*a  + 10*b) 
d = n - (1000*a + 100*b + 10*c)
print(a, b, c, d, sep = "\n") 
