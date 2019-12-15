'''
Q15. Implement a program that requests four numbers (integer or floating-point) from the user. Your program should 

compute the average of the first three numbers and compare the average to the fourth number. If they are equal, your 

program should print 'Equal' on the screen.

Test Data:

Enter first number: 4.5

Enter second number: 3

Enter third number: 3

Enter last number: 3.5

Expected Output: Equal
'''
[print("\nEqual") for i in range(1) if sum([float(input(f"enter n{i+1}: ")) for i in range (3)])/3 == float(input(f"enter n{4}: "))]
