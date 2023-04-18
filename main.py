import os

def send(number: str, message: str):
    os.system(f'adb shell service call isms 7 i32 1 s16 "com.android.mms.service" s16 "{number}" s16 "null" s16 "{message}" s16 "null" s16 "null"')
