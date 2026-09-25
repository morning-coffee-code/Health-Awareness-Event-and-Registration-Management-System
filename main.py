students = []
campaign = [
	{"Name":"Health Awareness Camp","Date":"03-10-2026","Time":"10:30 AM","Venue":"AB1 Audi 1"},{"Name": "Nutrition Awareness Camp", "Date":"03-10-2026","Time": "12:30 PM","Venue":"AB1 Audi 1"},
	{"Name": "Mental Health Awareness Campaign", "Date": "03-10-2026", "Time": "2:30 PM","Venue":"Academic Block 3 1st Floor"},
	{"Name":"Blood Donation Camp","Date":"03-10-2026","Time":"4:30 PM","Venue":"Open Audi"},
	{"Name": "Drug Abuse Prevention and Awareness Campaign","Date": "04-10-2026", "Time":"10:30 AM","Venue":"Open Auditorium"},
]
#TO REGISTER
def Register_student():
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

# TO SHOW HEALTH AWARENESS
def displayHealthAwareness():
	print("_____HEALTH AWARENESS INFORMATION_____")
	print("1. be hygenic.")
	print("2. eat a balanced diet.")
	print("3. be physically active. ")

	print ("4. don't eat from outside. ")
	print("5. drink enough water. ")
	print("6. have a complete 8 hours of sleep.")
	print("7. seek professional help if needed.")
	print("8. do not rely on apps like youtube and google for diagonosis.")

def viewCAMPAIGN():
	print("____UPCOMING HEALTH CARE CAMPAIGN_____")
	for i , camp in enumerate(campaign , start=1 ):
		print("CAMPAIGN", i)
		print("campaingn", i)
		print("Name:" , camp["Name"])
		print("Date:" , camp["Date"])
		print("Time:" , camp["Time"])
		print("Venue:", camp["Venue"])

def registerCAMPAIGN():
	print("____CAMPAIGN REGISTRATION_____")

	if len(students) == 0:
		print("please register as student first")
		return

	roll_no = str(input("Enter your registrtation number "))

	matching_stu = None
	for s in students:
		print(s.keys())
		if s ["Registration_no"] == roll_no:
			matching_stu = s
			break


	if matching_stu is None:
		print("Registratinon number not found.")
		return

	viewCAMPAIGN()
	try:
		choice = int (input("enter the campaign number you want to register"))
		selected_camp = campaign[choice - 1]
	except(ValueError, IndexError):
		print("Invalid number")
		return



	print(f"{matching_stu['Name']} successfully registered for '{selected_camp['Name']}'!")


def display_stu():
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

while True:
	print("===============================")
	print("    Health care campaign")
	print("===============================")
	print("1. Student Registration")
	print("2. Show Health Awareness Information")
	print("3. View Campaigns")
	print("4. Register for a Campaign")
	print("5. Display Registered Students")
	print("6. Exit")

	choice = input("Enter your choice: ")
	if choice == "1":
		Register_student()

	elif choice == "2":
		displayHealthAwareness()

	elif choice == "3":

		viewCAMPAIGN()
	elif choice =="4":

		registerCAMPAIGN()

	elif choice == "5":

		display_stu()
	elif choice == "6":
		
		print("take care of you health <3 and eat healthy")
		break
	else:
		print("Invalid choiece")
