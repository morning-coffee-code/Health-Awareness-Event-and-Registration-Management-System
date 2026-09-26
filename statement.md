## Problem Statement

Educational institutions often organize fitness-related awareness programs. These include health check-up camps, nutrition awareness drives, mental health events, blood donation camps and drug abuse prevention initiatives. However keeping track of student participation in these events is usually done manually using paper registers or scattered spreadsheets. This makes it hard to:

- Know which students are registered on campus and active

- Let students view all campaigns in one place

- Allow students to sign up for specific campaigns using their unique registration number

- Maintain an easily accessible list of who has signed up

This project solves this issue by offering a simple command-line based system. Students can sign in view fitness campaigns and join the ones they want. Campaign organizers can see the list of registered students. All this works through a terminal tool with no external database or GUI setup.

## Scope of the Project

This project is a *console-based (CLI) application* written in Python that includes:

- Registering students with their name, registration number, department and hosteller/day-student status

- Sharing current health awareness suggestions and tips with students

- Displaying all upcoming fitness campaigns with their name, date, time and venue

- Letting an already-registered student join a specific campaign using their registration number

- Displaying the complete list of currently registered students

**Not included** in this version:

- Data storage. All data is stored in memory during the session only. Is lost when the system ends (no database or file storage)

- User authentication or login system

- A graphical user interface (GUI) or web-based interface

- The ability to change or remove a student’s registration once submitted

- Alerts or reminders for upcoming campaigns

## Target Users

- **Students** who are part of the institution and want to register themselves and sign up for one or more health awareness campaigns

- **Campaign organizers or administrators** (such as student health committee members or event coordinators) who need a way to see the list of students who have signed up either for the entire event or for a specific campaign

## High-Level Features

1. **Student Registration**. Collect a student’s name, registration number, branch and residence type (hosteller or day student). Save this information for the session.

2. **Health Awareness Information**. Share a list of health tips (hygiene, diet, physical activity, sleep, mental health, etc.) to raise awareness among students.

3. **View Campaigns**. Show all health-related campaigns in a numbered list with details: name, date, time and venue.

4. **Campaign Registration**. Let a student, identified by their registration number sign up for a campaign, from the list of events.

5. **View Registered Students**. Show a list of all registered students with their details.

6. **Simple Menu-Driven Interface**. A looped, numbered menu system that allows users to move between features during a terminal session until they choose to exit.