# Health-Awareness-Event-and-Registration-Management-System
A command-line Python application to manage student registrations and sign-ups for campus health awareness campaigns.
# Health Care Campaign Management System

This is a command-line Python program that helps manage student registrations and health awareness campaign sign-ups on campus.

## Features

- Register a student with name, registration number, branch and hosteller or day scholar status

- Show general health awareness information to students

- List upcoming health campaigns with date, time and venue

- Let an already registered student sign up for a specific campaign

- Display all students who have registered so far

## Requirements

- Python 3.7 or higher

- No external packages are needed. The project only uses Python’s built-in tools

## Environment Setup

1. **Check that Python is installed:**

```bash

python3 --version

```

If Python is not installed go to https://www.python.org/downloads/ to download it.

2. **Clone the repository:**

```bash

git clone https://github.com/{your-username}/{your-repo-name}

cd {your-repo-name}

```

3. **(Optional but recommended) Create and activate an environment:**

```bash

python3 -m venv venv

source venv/bin/activate      # On macOS/Linux

venv\Scripts\activate         # On Windows

```

## Dependency Installation

The project does not use any external packages. If `requirements.txt` is added later install dependencies using:

```bash

pip install -r requirements.txt

```

## Configuration

There are no configuration files API keys or environment variables required to run this program.

## Running the Project

Run the program from the terminal with:

```bash

python3 main.py

```

You will see a menu:

```

===============================

Health care campaign

===============================

1. Student Registration

2. Show Health Awareness Information

3. View Campaigns

4. Register for a Campaign

5. Display Registered Students

6. Exit

```

Enter the number of the action you want to do. Follow the instructions shown on the screen. Choose option `6` to quit the program.

### Example Usage

1. Pick option `1` to register as a student. You'll be asked to enter your name, registration number, branch and whether you're a hosteller or a day scholar.

2. Pick option `3` to see the list of health campaigns.

3. Pick option `4` to sign up for one of the campaigns by entering your registration number.

4. Pick option `5` anytime to see all students who are currently registered.

## Notes

- All data like student details are kept in memory only. Every time you restart the program the data is lost. There is no database or file to save the data.

- The list of campaigns is written directly in `main.py`. If you need to add a campaign just edit the `campaign` list, in the code.

## Project Structure

```

your-repo-name/

├── README.md

├── requirements.txt

├──.gitignore

└── main.py

```
