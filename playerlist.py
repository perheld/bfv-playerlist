from lib import BFV
import requests
import time
import json


if __name__ == "__main__":
    print("[+] Searching for BFV.exe")
    phandle = BFV.get_handle()
    if phandle:
        time.sleep(1)
    else:
        print("[-] Error: Cannot find BFV.exe")
        exit(1)
    print("[+] BFV.exe found, Handle 0x%x" % phandle)

    cnt = 0
    headers = {'Accept': 'application/json'}

    while True:
        try:
            BFV.process(phandle, cnt, 0x8)
            cnt += 1

            data = BFV.gamedata

            if not data.soldiers:
                continue

            print("-" * 20)

            for s in data.soldiers:
                if isinstance(s.name, str):
                    r = requests.get('https://bfvhackers.com/api/v1/is-hacker?name=' + s.name + '&stats=false', headers=headers)

                    # if its not OK just continue on with the others, possibly we are ratelimited
                    if r.status_code != 200:
                        continue

                    json_data = json.loads(r.text)

                    if not json_data['hack_level']:
                        continue

                    if json_data['hack_level'] != "legit":
                        print("https://bfvhackers.com/?name=" + s.name + ": " + json_data['hack_level'])
        except Exception as e:
            print(e)
            continue

        time.sleep(10)
