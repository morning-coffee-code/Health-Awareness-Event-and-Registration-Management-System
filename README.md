# Health-Awareness-Event-and-Registration-Management-System
A command-line Python program to run registration and sign-up for campus health awareness campaigns.
# Health Care Campaign Management System
This is a command-line Python program that registers students to attend a health awareness campaign on campus.
Features
- Submit a Student registration with name, registration number, branch and hosteller/day scholar?
- Present general health awareness information to students
- Upcoming health promotion campaigns and activities (Date, time and venue)
- Have a previously enrolled student register to a pre-selected campaign
- Show all registered students to date
Requirements
- Python 3.7 or higher
- No third-party packages are required. The code only depends on Python's standard library
Environment Setup
1. Check that Python is installed:
``bash
python3 --version
`
If Python is not installed, go to https://www.python.org/downloads/ to install it.
2. Clone the repository:
`bash
git clone https://github.com/{your-username}/{your-repo-name}
cd {your-repo-name}
`
3. (Optional but strongly recommended) Make environment and activate it:
`bash
python3 -m venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows
`
Dependency Installation
This project does not depend on any external packages. If you add requirements.txt later, then install dependencies with:
`bash
pip install -r requirements.txt
`
Configuration
This program uses no configuration files or environment variables or API keys.
Running the Project
Run the program from the terminal with:
`bash
python3 main.py
`
You will see a menu:
`
===============================
Health care campaign
===============================
1. Student Registration
2. Show Health Awareness Information
3. View Campaigns
4. Register for a Campaign
5. Display Registered Students
6. Exit
`
Type the action number you wish to do. Follow the directions on the screen. Select 6 to exit out of the program.
### Example Usage
1. Select option 1' - Register as a student On asking for name, registration number, branch and type of student - hosteller or day scholar.
2. Select option 3 and there will be health campaigns.
3. Select 4 to register on one of the campaigns by inputting your registration number.
4. To find out who is currently enrolled, always select 5.
Notes
- Everything is only in memory such as: the students' data. And it is all lost every time you run the program again. There are no database or files that saved the data.
- Campaigns list is written in main.py as is. If you would like to add a campaign, simply add in main.py campaign list.
Project Structure
``
your-repo-name/
README.md
requirements.txt
.gitignore
main.py
`
Module Names
`all module name-
1. Register_student.py
2. DisplayHealthAwareness.py
3. Display_stu.py
4. Registercampaign.py
5. ViewCAMPAIGN.py
``
