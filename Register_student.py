#TO REGISTER

def Register_student(students):
	print("___________student registration___________")

	name = str(input("Enter Student's name "))
	reg_no = str( input("Enter registration number here... "))
	Branch = str(input("Enter branch name "))
	student_type = str(input(" hosteller/ day scholler "))
	student = {
		"Name": name,
		"Registration_no": reg_no,
		"Branch": Branch,
		"Student_type": student_type
	}
	#now append in student
	students.append(student)
	print("REGISTRATION SUCCESSFULL!!!")