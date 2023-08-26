import requests
import base64
import itertools
import string
import threading
import time

accid = ""  # Account ID, Find it by looking your user up on GDBrowser
pw = ""  # Your password in plain text
subject = ""  # Message subject
body = ""  # Message body

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, itertools.cycle(key)))

def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

def gjp_encrypt(data):
    return base64.b64encode(xor(data, "37526").encode()).decode()

def message_encode(data):
    return base64_encode(xor(data, '14251'))

def getAccountID():
    userid = requests.post(
        "http://www.boomlings.com/database/getGJLevels21.php",
        data={"type": "4", "secret": "Wmfd2893gb7"},
        headers={"User-Agent": ""},
    ).text.split(":")[7]
    return requests.post(
        "http://www.boomlings.com/database/getGJUsers20.php",
        data={"str": userid, "secret": "Wmfd2893gb7"},
        headers={"User-Agent": ""},
    ).text.split(":")[21]

def uploadMessage(id, pw):
    rr = requests.post(
        "http://www.boomlings.com/database/uploadGJMessage20.php",
        data={
            "accountID": accid,
            "gjp": gjp_encrypt(pw),
            "toAccountID": str(getAccountID()),
            "subject": base64_encode(subject),
            "body": message_encode(body),
            "secret": "Wmfd2893gb7",
        },
        headers={"User-Agent": ""},
    ).text
    if rr == "1":
        return "Success"
    else:
        return "User has messages turned off"

while True:
    print(str(uploadMessage(id, pw)))
    time.sleep(4)
