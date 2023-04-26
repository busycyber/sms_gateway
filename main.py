import os

def send(number: str, message: str):
    message_arg = f'"{message}"'.replace(" ", "\ ")

    # Call the adb shell service call command with the phone number and message text arguments
    try:
        os.system(f'adb shell service call isms 7 i32 1 s16 "com.android.mms.service" s16 "{number}" s16 "null" s16 {message_arg} s16 "null" s16 "null"')
    except Exception:
        try:
            os.system("adb kill-server")
            os.system("adb connect 192.168.0.30:5555")
        except Exception:
            pass

