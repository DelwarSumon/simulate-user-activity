<p align="center"><a href="https://github.com/DelwarSumon/simulate-user-activity" ><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/simulate_activity1.webp?raw=true" style=""></a></p>

## App Switcher with Simulated User Activity
This Python application allows users to simulate user interactions with multiple selected applications. It automates tasks like moving the cursor, scrolling within windows, and switching between apps seamlessly. The app is designed with a user-friendly GUI, enabling easy selection and customization of tasks.

## Features
- Select applications to automate from the file manager.
- Automatically switch between applications, bringing them to the foreground.
- Perform tasks like scrolling, moving the cursor, or navigating text editors.
- User-configurable time intervals for actions.
- Warnings displayed for missing or invalid inputs.
- A clean and intuitive graphical interface.

## Prerequisites
- Python (You can download from here https://www.python.org/downloads/)
- Libraries: (See `Install Required Dependencies` )
  - pyautogui (for simulating mouse and keyboard interactions).
  - PyGetWindow (for managing application windows).
  - pillow (for image handling in the GUI).
  - tkinter (pre-installed with Python, for building the GUI).
    
## Installation Procedure
#### Step 1: Clone the Repository
- git clone https://github.com/DelwarSumon/simulate-user-activity.git
- change your directory to simulate-user-activity (For windows - `cd simulate-user-activity`)

#### Step 2: Install Required Dependencies
- Install the necessary Python libraries:
```bash
pip install pyautogui PyGetWindow pillow
```

## How to Use

#### Step 1: Launch the App
- Run the application by executing:
```bash
python simulate_activity.py
```

#### Step 2: Select Applications
- Use the "Select Application" button to choose the `.exe` files of the applications you want to automate.
- The selected applications will be listed in the app window.

#### Step 3: Configure Settings
- Specify the duration for which actions should be performed per app (default is 10 seconds).
- The app will move the cursor, scroll, and interact with the selected applications as configured.

#### Step 4: Start and Stop Automation
- Run: Click the "Run" button to start the automation process.
- Stop: Click the "Stop" button to terminate the automation at any time.

#### Step 5: Close the App
- The app can be exited gracefully using the close button.

## Folder/File Structure
```CLEA
simulate-user-activity/
│
├── simulate_activity.py       # Main Python script
├── README.md                  # Documentation
```

## Screenshots

<p align="center"><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/Screenshot_1.png?raw=true"></p>
<p align="center"><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/Screenshot_2.png?raw=true"></p>
<p align="center"><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/Screenshot_3.png?raw=true"></p>
<p align="center"><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/Screenshot_.png?raw=true"></p>
<p align="center"><img src="https://github.com/DelwarSumon/simulate-user-activity/blob/main/screenshots/Screenshot_5.png?raw=true"></p>

***-- Have FUN --***
