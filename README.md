# Health-Awareness-Event-and-Registration-Management-System
A command-line Python application to manage student registrations and sign-ups for campus health awareness campaigns.
# Health Care Campaign Management System

A command-line Python application for managing student registrations and health
awareness campaign sign-ups on campus.

## Features

- Register a student (name, registration number, branch, hosteller/day scholar status)
- Display general health awareness information
- View upcoming health campaigns (date, time, venue)
- Register an already-enrolled student for a specific campaign
- Display all registered students

## Requirements

- Python 3.7 or higher
- No external/third-party packages are required — the project only uses Python's
  built-in standard library.

## Environment Setup

1. **Check Python is installed:**
   ```bash
   python3 --version
   ```
   If Python is not installed, download it from https://www.python.org/downloads/.

2. **Clone the repository:**
   ```bash
   git clone https://github.com/{your-username}/{your-repo-name}
   cd {your-repo-name}
   ```

3. **(Optional but recommended) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```

## Dependency Installation

This project has no external dependencies, but if `requirements.txt` is ever
extended in the future, install dependencies with:
```bash
pip install -r requirements.txt
```

## Configuration

No configuration files, API keys, or environment variables are required to run
this project.

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

Enter the number corresponding to the action you want to perform, and follow
the on-screen prompts. Choose option `6` to exit the program.

### Example Usage

1. Choose `1` to register as a student (enter name, registration number, branch,
   and hosteller/day scholar status).
2. Choose `3` to view the list of upcoming campaigns.
3. Choose `4` to register for one of the listed campaigns using your
   registration number.
4. Choose `5` at any time to view all currently registered students.

## Notes

- All data (students list) is stored in memory only and will reset each time
  the program is restarted — there is no persistent storage (database or file)
  in this version.
- The list of campaigns is hardcoded in `main.py` and can be edited directly in
  the `campaign` list if new campaigns need to be added.

## Project Structure

```
your-repo-name/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```
