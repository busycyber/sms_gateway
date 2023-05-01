# sms_gateway
GUI, for using ADB to send messages

This is a simple SMS sender application for Android phones using ADB (Android Debug Bridge) and PySimpleGUI. The application allows the user to enter a phone number and message text in a GUI and send the message directly from their computer via ADB to their Android phone.

## Learn
This project is a great way to learn how to use PySimpleGUI and the ADB command-line tool to interact with Android devices. By studying this codebase, you will learn:

How to use PySimpleGUI to create a simple graphical user interface (GUI) for Python applications
How to use the ADB command-line tool to send SMS messages to an Android phone
How to use environment variables to store configuration information for your applications
## Requirements
To use this application, you need:

Python 3.7 or higher
PySimpleGUI

## Installation

### Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```
### Install PySimpleGUI:
```
pip install PySimpleGUI
```
### Usage
1. Connect your Android phone to your computer via USB and enable USB debugging in the developer options.
2. Find out the IP address of your phone: `adb shell ifconfig wlan0`
3. Set the `PHONE_IP` environment variable to the IP address of your phone:

```arduino
export PHONE_IP=YOUR_PHONE_IP_ADDRESS
```
Run the GUI application:
```
python gui.py
```
or
```
python3 gui.py
```
5. In the GUI application, enter the recipients and message text, then click the Send button to send the message.

### main.py
```
python

import os

def send(number: str, message: str):
    message_arg = f'"{message}"'.replace(" ", "\ ")

    try:
        os.system(
            f'adb shell service call isms 7 i32 1 s16 "com.android.mms.service" s16 "{number}" s16 "null" s16 {message_arg} s16 "null" s16 "null"')
    except Exception:
        try:
            os.system("adb kill-server")
            os.system("adb connect 192.168.0.30:5555")
        except Exception:
            pass
  ```
This is the main Python script that sends the SMS message. It uses the os module to run the ADB command-line tool with the appropriate arguments to send the message to the specified phone number. If the ADB connection is lost, it will try to reconnect to the phone
