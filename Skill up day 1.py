#TEMPERATURE THEESOLD
C=float(input("Enter tempareture in degree centigrade:  "))
F=(9*C/5)+32
print("The tempareture in farenhite is: ",F)
if F<=32:
		print(" Freezing tempareture")
elif F>=95:
		print("Heatwave")
else:
		print("Normal tempareture")
		
		
		
#PASS OR FAIL
B=int(input("Your marks in bengali is:  "))
E=int(input("Your marks in english is:  "))
M=int(input("Your marks in Math is:  "))
Avg=(B+E+M)/3
if B<35 or E<35 or M<35 or Avg<40 :
	print("Better Luck Next Time")
else:
	print("Congrats!! you passed")
