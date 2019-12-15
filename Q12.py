'''
Q12. Write a Python program that allows the user to enter any number of nonnegative floating-point values. The user terminates the input list with any negative value. The program then prints the sum, average (arithmetic mean), maximum, and minimum of the values entered. The terminating negative value is not used in the computations.
'''
sum = 0
max = float("-inf")
min = float("inf")
count = 0
print("Enter numbers(-ve value to terminate):")
while float("inf"):
	num = float(input(">>>"))
	if num >= 0:
		count += 1
		sum += num
	
		if num > max:
			max = num
			
		if num < min:
			min = num
		
	else:
		print("sum =", sum)
		print("average =", sum/count)
		print("max =", max)
		print("min =", min)
		break
