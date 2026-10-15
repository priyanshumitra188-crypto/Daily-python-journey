#-------------------------------
#Pass or fail with list and loop
#-------------------------------
n=int(input("Enter number of subjects :  "))
marks=[]
for i in range(n):
	score=int(input("Enter the marks:  "))
	marks . append(score)
total=sum(marks)
avg=total/n
highest=max(marks)
lowest=min(marks)
passed=True 
for s in marks:
	if s<35:
		passed=False
if s>=35 and avg>=40:
	print("passed")
else:
	print("better luck next time")

	
		
		
		













