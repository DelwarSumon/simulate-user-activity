import subprocess
import pyautogui
import pygetwindow as gw
import time
import random
import tkinter as tk
from tkinter import filedialog, Frame, Label, Checkbutton, IntVar, Spinbox, Scrollbar, Listbox, messagebox
from threading import Thread, Event
from PIL import Image, ImageTk

apps = []  # Initialize an empty list to hold selected apps
stop_event = Event()  # Event to signal threads to stop

def extract_app_name(window_title):
    """Extract the actual application name from the window title."""
    return window_title.split('-')[-1].strip()  # Get the last part after the hyphen

def open_or_focus_app(app_name, command):
    """Open the app if not open, otherwise bring the open app to the foreground."""
    windows = gw.getWindowsWithTitle(app_name)  # Get windows with the title that includes app_name
    if windows:
        window = windows[0]  # Focus the first found window
        window.activate()  # Bring the window to the front
        return window.title  # Return the window title
    else:
        subprocess.Popen(command)  # Open the application
        time.sleep(3)  # Give time for the app to open
        return open_or_focus_app(command.split("/")[-1], command)  # Retry to find the window

def move_cursor_in_editor(app_name):
    """Move the cursor using arrow keys and Ctrl + G for specified editors."""
    editors = ["Notepad", "Sublime Text", "Visual Studio Code", "PyCharm", "PHPStorm"]
    
    if any(editor in app_name for editor in editors):
        direction = random.choice(["up", "down", "goto"])
        if direction == "up":
            pyautogui.press("up")
        elif direction == "down":
            pyautogui.press("down")
        elif direction == "goto":
            line_number = random.randint(1, 1000)
            pyautogui.hotkey("ctrl", "g")
            time.sleep(0.2)
            pyautogui.typewrite(str(line_number))
            pyautogui.press("enter")
    else:
        direction = random.choice(["up", "down"])
        if direction == "up":
            pyautogui.press("up")
        else:
            pyautogui.press("down")

def scroll_within_window():
    """Scroll vertically within the window."""
    scroll_amount = random.choice([-300, -600, -900, 300, 600, 900])
    pyautogui.scroll(scroll_amount)

def simulate_activity(selected_app, duration):
    """Simulate activity by switching to the selected application indefinitely."""
    app_name, command = selected_app
    while not stop_event.is_set():  # Check for stop signal
        window_title = open_or_focus_app(app_name.split('.')[0], command)  # Get the actual window title
        # print(app_name)
        # print(app_name.split('.')[0])
        # print(window_title)
        # Repeat actions for 10 seconds, moving and scrolling every 3 seconds
        start_time = time.time()
        while time.time() - start_time < duration and not stop_event.is_set():
            move_cursor_in_editor(window_title)  # Use the actual window title
            scroll_within_window()
            time.sleep(3)

# Generalized function to show a warning or notification message at the top            
def show_warning_message(text, color="red", duration=3000, font=("Arial", 10)):
    warning_label.config(text=text, fg=color, font=font)
    warning_label.pack()  # Display the warning label

    # Hide the warning label after the specified duration
    root.after(duration, lambda: warning_label.pack_forget())

def run_simulation():
    """Run the simulation for all selected applications."""
    selected_indices = app_listbox.curselection()  # Get the indices of selected items
    duration = int(duration_input.get())

    # Check if no applications are selected
    if not selected_indices:
        # messagebox.showwarning("No Application Selected", "You do not select any application")
        show_warning_message("You did not select any application", color="red", duration=3000)
        return

    stop_event.clear()  # Clear the stop event
    for index in selected_indices:
        app = apps[index]
        thread = Thread(target=simulate_activity, args=(app,duration))
        thread.daemon = True  # Daemonize thread to exit when main program exits
        thread.start()

def select_app():
    """Open a file dialog to select multiple application executables."""
    app_paths = filedialog.askopenfilenames(filetypes=[("Executable Files", "*.exe")])
    for app_path in app_paths:
        app_name = app_path.split("/")[-1]  # Get the name of the executable
        apps.append((app_name, app_path))  # Add app to the apps list
        app_listbox.insert(tk.END, app_name) # Insert app names into the listbox 
        app_listbox.selection_set(tk.END) # Select the newly added app

def stop_simulation():
    """Stop the simulation by signaling all threads to stop and close the application window."""
    stop_event.set()  # Set the stop event to signal threads to stop
    root.destroy()  # Close the main application window

# Create the main application window
root = tk.Tk()
root.title("Simulate Activity")
root.geometry("600x400")  # Set window size

# Configure window style
root.configure(bg="#f0f0f0")

# Load the background image
# background_image_path = "bg.jpg"  # Replace with your image file path
# background_image = Image.open(background_image_path)
# background_image = background_image.resize((600,400), Image.LANCZOS)  # Resize to fit window
# background_photo = ImageTk.PhotoImage(background_image)

# # Display the image as a background in a label
# background_label = Label(root, image=background_photo)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Main container frame on top of background image
# container = Frame(root, bg="")  # Make it semi-transparent if needed
# container.pack(fill="both", expand=True, padx=10, pady=10)

# Warning label setup (initially hidden)
warning_label = Label(root, text="")
warning_label.pack_forget()  # Keep hidden initially

# Create a button to select applications
select_button = tk.Button(root, text="Select Applications", command=select_app, bg="#4CAF50", fg="white", font=("Arial", 12), relief=tk.RAISED)
select_button.pack(pady=15, padx=15)

# Create a Listbox for app selection
app_label = tk.Label(root, text="Selected applications:", bg="#f0f0f0", font=("Arial", 12))
app_label.pack(pady=5)

# app_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10, font=("Arial", 12), bg="#fff", selectbackground="#4CAF50")  # Multi-select listbox
# app_listbox.pack(pady=10)

# Create a Listbox with vertical scrollbar
listbox_frame = Frame(root, bg="#f0f0f0")
listbox_frame.pack(pady=5)
scrollbar = Scrollbar(listbox_frame, orient=tk.VERTICAL)
app_listbox = Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=50, height=6, yscrollcommand=scrollbar.set, font=("Arial", 10))
scrollbar.config(command=app_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
app_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

duration_label = Label(root, text="Stay in each application - Duration (seconds):", bg="#f0f0f0", font=("Arial", 12))
duration_label.pack(pady=5)
duration_input = Spinbox(root, from_=1, to=600, width=5, font=("Arial", 12))
duration_input.pack(pady=5)
duration_input.delete(0, "end")
duration_input.insert(0, "10")  # Default duration is set to 10 seconds

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

# Create a run button
run_button = tk.Button(button_frame, text="Run", command=run_simulation, bg="#2196F3", fg="white", font=("Arial", 12), relief=tk.RAISED)
run_button.pack(side=tk.LEFT, padx=10)

# Create a stop button
stop_button = tk.Button(button_frame, text="Stop", command=stop_simulation, bg="#f44336", fg="white", font=("Arial", 12), relief=tk.RAISED)
stop_button.pack(side=tk.LEFT, padx=10)

# Start the GUI event loop
root.mainloop()
