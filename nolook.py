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

    players = {}

    while True:
        time.sleep(10)

        with open("listofplayers.txt", 'w') as f:  
            for key, value in players.items():  
                f.write('%s\n' % (key))

        try:
            print("-" * 20)

            BFV.process(phandle, cnt, 0x8)
            cnt += 1

            data = BFV.gamedata

            if not data.soldiers:
                continue

            for s in data.soldiers:
                if isinstance(s.name, str):
                    print(s.name)
                    players[s.name] = s.name

        except Exception as e:
            continue
