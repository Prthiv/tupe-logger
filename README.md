=========================================
                Tupe-Logger
=========================================
A Keystroke Logger Tool for Educational Purposes

**DISCLAIMER:**
This tool is for educational purposes only.
Unauthorized use is illegal and unethical.
Use this tool only with explicit consent from the target system's user.

=========================================
Overview:
=========================================
Tupe-Logger is a simple Python-based keylogger tool that captures keystrokes from a target system and sends the captured data to a specified email address. It is designed for educational purposes to demonstrate how keylogging can be implemented. It is important to note that **this tool must only be used in environments where explicit permission is granted**.

=========================================
How the Tool Works:
=========================================
1. **Keylogging**: The tool listens for keyboard input on the system where it is executed. Each keystroke is captured and saved to a log file (`keylog.txt`).
   
2. **Email Reporting**: The captured keystrokes are then sent to the specified email address in real time. You will need to configure the sender and receiver email addresses in the script before use.

3. **Packaging**: The tool can be packaged into a standalone executable (.exe for Windows) using **PyInstaller**, which makes it easier to distribute the tool.

4. **Logs**: Keystrokes are saved in a log file and can be viewed at any time by opening the `keylog.txt` file. The tool also sends the captured keystrokes to the email you specify.

=========================================
Installation & Setup Instructions:
=========================================
1. **Clone or Download Tupe-Logger**:
   - Clone the repository or download the Python script (`keylogger.py`) to your local machine.

2. **Install Python**:
   - Make sure you have Python 3.x installed on your machine. Download it from https://www.python.org/downloads/.

3. **Install Dependencies**:
   - Open a terminal or command prompt.
   - Navigate to the directory where you downloaded Tupe-Logger.
   - Install the required dependencies by running the following command:
     ```
     pip install -r requirements.txt
     ```
   This will install the necessary Python libraries (`pynput`, `pyinstaller`, etc.) to run the tool.

4. **Configure Email Credentials**:
   - Open the `keylogger.py` script.
   - Configure the email addresses in the script (sender, receiver), as well as the email password (use an app password if using Gmail).
   - Example configuration:
     ```python
     SENDER_EMAIL = "your_email@example.com"
     SENDER_PASSWORD = "your_email_password"  # Use an app password if using Gmail
     RECEIVER_EMAIL = "receiver_email@example.com"
     ```

5. **Running the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `keylogger.py` is located.
   - Run the script with the following command:
     ```
     python keylogger.py
     ```
   - The script will start the keylogger and begin logging keystrokes.

6. **Automating the Packaging**:
   - If you want to package the script into a standalone executable file, you can select the **"Automate PyInstaller"** option from the menu within the tool. This will create a `.exe` file without requiring you to manually invoke PyInstaller.

7. **View the Keystroke Logs**:
   - The keystroke data is saved in the `keylog.txt` file.
   - You can view the captured keystrokes by opening the file with any text editor.
   - The tool will also send the keystrokes to the receiver's email address as they are captured.

=========================================
Using the Tool:
=========================================
After running the script, you will be presented with a menu that offers several options:

1. **Configure Email Credentials**: Configure your email settings (sender's and receiver's email addresses).
2. **Run Tupe-Logger (Start Keylogging)**: Start the keylogger, which will begin logging keystrokes.
3. **View Keystroke Logs**: View the logged keystrokes in the `keylog.txt` file.
4. **Automate PyInstaller (Create Executable)**: Automatically convert the Python script into a standalone executable using PyInstaller.
5. **Exit**: Exit the program.

**Important Notes:**
- **Always ensure you have explicit consent** from the target machine's user before using this tool.
- **Do not use this tool for malicious or unethical activities**. Unauthorized keylogging is illegal and punishable by law.
- The tool captures all keystrokes including passwords and other sensitive information, so it should only be used in safe, educational, or ethical environments.

=========================================
Version: 1.0
Date: January 2025
=========================================
