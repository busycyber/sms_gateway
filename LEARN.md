## Learn

### Requirements

To use this application, you need:

-   Python 3.7 or higher
-   PySimpleGUI

### Installation

1. Clone this repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

2. Install PySimpleGUI:

pip install PySimpleGUI

### Usage

1. Connect your Android phone to your computer via USB and enable USB debugging in the developer options.

2. Find out the IP address of your phone:
   adb shell ifconfig wlan0

3. Set the `PHONE_IP` environment variable to the IP address of your phone:

export PHONE_IP=YOUR_PHONE_IP_ADDRESS

4. Run the GUI application:

`python gui.py` or `python3 gui.py`

5. In the GUI application, enter the recipients and message text, then click the `Send` button to send the message.
