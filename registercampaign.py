from viewCAMPAIGN import viewCAMPAIGN

def registerCAMPAIGN(students, campaign):
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

	viewCAMPAIGN(campaign)
	try:
		choice = int (input("enter the campaign number you want to register"))
		selected_camp = campaign[choice - 1]
	except(ValueError, IndexError):
		print("Invalid number")
		return



	print(f"{matching_stu['Name']} successfully registered for '{selected_camp['Name']}'!")