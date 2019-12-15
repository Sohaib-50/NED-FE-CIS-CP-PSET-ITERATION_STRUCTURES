'''Q11. Write a Python program that allows the user to enter exactly twenty floating-point values. The program then prints the 
sum, average (arithmetic mean), maximum, and minimum of the values entered.
'''
#solution0:
nums = ""
for i in range(1, 20):
#concatenating nums with the string form of input number followed by a comma so we can later seperate the numbers out
	nums += input(f"num{i}: ") + ","

sum = 0
max = float("-inf")
min = float("inf")
n = ""
#traverse nums and while character is not a ","(comma), keep concatenating the variable with ch. As soon as a comma is encountered, else block is entered where n is converted from string to float and then it is added to sum, determined if its the biggest number encountered so far and if its the smallest number encountered. then n is made into an empty string again so we can repeat the process to get the next number.
for ch in nums:
	if ch != ",":
		n += ch
	else:
		n = float(n)
		sum += n
		
		if n > max:
			max = n
		
		if n < min:
			min = n
		n = ""
		
print("sum =", sum)
print("average =", sum/4)
print("max =", max)
print("min =", min)
		
#solution1:
sum = 0
max = float("-inf")
min = float("inf")


for i in range(1, 21):
	num = float(input(f"enter n{i+1}: "))

	sum += num

	if num > max:
		max = num
		
	if num < min:
		min = num
		
print("sum =", sum)
print("average =", sum/20)
print("max =", max)
print("min =", min)
		
