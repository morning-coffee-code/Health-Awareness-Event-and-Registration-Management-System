# **Health Care Campaign Management System**



This Health Care Campaign Management System is a Python application that manages student registrations and sign‑ups for health awareness campaigns on campus.



## **Features**



1.Health Care Campaign Management System registers a student with name, registration number, branch and hosteller or day scholar status



2.Health Care Campaign Management System shows general health awareness information



3.Health Care Campaign Management System displays health campaigns with date, time and venue



4.Health Care Campaign Management System registers a student who is already enrolled for a particular campaign



5.Health Care Campaign Management System shows all registered students



## **Requirements**



Python 3.7 or higher is required



No external or third‑party packages are needed. The Health Care Campaign Management System uses Python’s built‑in standard library



## **Environment Setup**



1. **Check Python is installed:**

```bash

&#x20;  python3 --version

If Python is not installed download it from https://www.python.org/downloads/.

```



**2. (Optional but recommended) Create and activate a virtual environment:**



```bash



python3 -m venv venv



source venv/bin/activate      # On macOS/Linux



venv\\Scripts\\activate         # On Windows



```



**Dependency Installation**



This project has no dependencies but if requirements.txt is ever extended in the future install dependencies with:



```bash



pip install -r requirements.txt



```



#### **Configuration**



**No configuration files API keys or environment variables are required to run this project.**



### **Running the Project**



Run the program from the terminal with:



```bash



python3 main.py  



```



**You will see a menu:**



```



===============================



Health care campaign



===============================



1\. Student Registration



2\. Show Health Awareness Information



3\. View Campaigns



4\. Register for a Campaign



5\. Display Registered Students



6\. Exit



```



Enter the number that matches the action you want to perform then follow the prompts shown on screen. Choose option 6 to exit the program.



**Example Usage**



Select 1 to register a student by entering name, registration number, branch and hosteller or day scholar status.



Select 3 to see the list of campaigns.



Select 4 to register for a campaign from the list using your registration number.



Select 5 at any time to view all students who are currently registered.



**Notes**



All data, such, as the list of students is kept in memory and will be lost each time the program restarts. The Health Care Campaign Management System does not use a database or file to store data.



The list of campaigns is hard‑coded in main.py. It can be edited directly in the campaign list if new campaigns must be added.



**Project Structure**



Health-Awareness-Event-and-Registration-Management-System/



├── README.md



├── requirements.txt



├──.gitignore



└── main.py

