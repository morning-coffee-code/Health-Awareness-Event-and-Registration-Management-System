from Register_student import Register_student
from displayHealthAwareness import displayHealthAwareness
from viewCAMPAIGN import viewCAMPAIGN
from display_stu import display_stu
from registercampaign import registerCAMPAIGN 



students = []
campaign = [
	{"Name":"Health Awareness Camp","Date":"03-10-2026","Time":"10:30 AM","Venue":"AB1 Audi 1"},{"Name": "Nutrition Awareness Camp", "Date":"03-10-2026","Time": "12:30 PM","Venue":"AB1 Audi 1"},
	{"Name": "Mental Health Awareness Campaign", "Date": "03-10-2026", "Time": "2:30 PM","Venue":"Academic Block 3 1st Floor"},
	{"Name":"Blood Donation Camp","Date":"03-10-2026","Time":"4:30 PM","Venue":"Open Audi"},
	{"Name": "Drug Abuse Prevention and Awareness Campaign","Date": "04-10-2026", "Time":"10:30 AM","Venue":"Open Auditorium"},
]


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
	print("================================")

	choice = input("Enter your choice: ")
	if choice == "1":
		Register_student(students)

	elif choice == "2":
		displayHealthAwareness()

	elif choice == "3":

		viewCAMPAIGN(campaign)
	elif choice =="4":

		registerCAMPAIGN(students, campaign)

	elif choice == "5":

		display_stu(students)
	elif choice == "6":
		
		print("take care of you health <3 and eat healthy")
		break
	else:
		print("Invalid choiece")
