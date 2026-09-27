
def viewCAMPAIGN(campaign):
	print("____UPCOMING HEALTH CARE CAMPAIGN_____")
	for i, camp in enumerate(campaign, start=1 ):
		print("CAMPAIGN", i)
		print("campaingn", i)
		print("Name:" , camp["Name"])
		print("Date:" , camp["Date"])
		print("Time:" , camp["Time"])
		print("Venue:", camp["Venue"])
	