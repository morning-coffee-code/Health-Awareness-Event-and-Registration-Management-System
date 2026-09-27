
def display_stu(students):
	print("_____Resgistration number_____")
	if len(students)== 0:
		print("No student registered yet.")
		return 
	for i, s in enumerate (students , start= 1):
		print(f"student {i}")
		print("Name : ", s["Name"])
		print("Registration number :", s["Registration_no"])
		print("Branch :",s["Branch"])
		print("Type:", s["Student_type"])