from lib import BFV
import time


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
        
    while True:
        BFV.process(phandle, cnt, 0x8)
        cnt += 1

        data = BFV.gamedata
        if not data.soldiers:
            continue
        print("-" * 20)
        for s in data.soldiers:
            if isinstance(s.name, str):
                print("https://bfvhackers.com/?name=" + s.name)

        time.sleep(5)
