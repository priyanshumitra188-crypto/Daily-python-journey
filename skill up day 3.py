#automated subject report card
n=int(input("Enter the number of subjects: "))
report_card={}
for i in range (n):
	subject=input("Enter name of the subject: ")
	score=int(input("Enter marks: "))
	report_card[subject]=score

avg=sum(report_card . values())/n
failed_subject =[]
for subject, score in report_card.items():
	if score<35:
		failed_subject.append(subject)

highest_score=-1
highest_subject=""
lowest_score=101
lowest_subject=""
for subject,score in report_card . items():
	if highest_score<score:
		highest_score=score
		highest_subject=subject
	if lowest_score>score:
		lowest_score=score
		lowest_subject=subject
print("overall average: ",avg)
if len(failed_subject)>0 or avg<40:
		print("Need improvement")
		print("failed in: ",failed_subject)
else:
		print("passed")
		print("Top subject: ",highest_subject,"with score: ",highest_score)
		print("weakest subject: ",lowest_subject,"with score: ",lowest_score)
		
	    

















