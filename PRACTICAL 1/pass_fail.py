def grades(c,marks):
	if any (mark<40 for mark in marks):
		print("Fail")
		return 0
	AP = (sum(marks)/(c*100))*100
	if AP>75:
		print(f"Aggregate Percentage: {AP:.2f}")
		print("Grade: Distinction")
	elif AP>=60 and AP<75:
		print(f"Aggregate Percentage: {AP:.2f}")
		print("Grade: First Division")
	elif AP>=50 and AP<60:
		print(f"Aggregate Percentage: {AP:.2f}")
		print("Grade: Second Division")
	elif AP>=40 and AP<50:
		print(f"Aggregate Percentage: {AP:.2f}")
		print("Grade: Third Division")

courses= int(input())
marks = list(map(int,input().split()))
grades(courses,marks)