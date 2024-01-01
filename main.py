import requests, base64, itertools, string, threading, time, random

threads = 25
accid = "" # get from gdbrowser
passw = "" # password
subject = "hi"
body = "my name is quandale dingle rehehehehehe"

def xor(data, key): return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, itertools.cycle(key)))
def base64_encode(string: str) -> str: return base64.urlsafe_b64encode(string.encode()).decode()
def gjp_encrypt(data): return base64.b64encode(xor(data, "37526").encode()).decode()
def message_encode(data): return base64_encode(xor(data, '14251'))

def doomsday(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

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

def uploadMessage(victim):
    try:
        proxy = doomsday('proxies.txt').strip()

        rr = requests.post(
            "http://www.boomlings.com/database/uploadGJMessage20.php",
            data={
                "accountID": accid,
                "gjp": gjp_encrypt(passw),
                "toAccountID": victim,
                "subject": base64_encode(subject),
                "body": message_encode(body),
                "secret": "Wmfd2893gb7",
            },
            headers={"User-Agent": ""},
            proxies={'http': "http://" + proxy, 'https': "https://" + proxy},
            timeout=4
        ).text

        if rr == "1":
            print(f"Success - Victim: {victim}")
        else:
            pass
    except Exception as e:
        pass

def lmao(account):
    for _ in range(threads):
        threading.Thread(target=uploadMessage, args=(account,)).start()

while True:
    account = getAccountID()
    lmao(account)
    time.sleep(4)
