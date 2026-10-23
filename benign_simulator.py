# CYB 301 - BENIGN MALWARE BEHAVIOUR SIMULATOR
# This program is intentionally non-destructive

from pathlib import Path
import platform
import socket
import time
import urllib.parse
import urllib.request

# Below are the values that should be modified by students

LAB_SERVER = "http://replace_with_receiver_ip:8000"

STUDENT_TAG = "name of the student"

MARKER_FILENAME = "CYB301_TEST.txt"

TEST_MESSAGE = "CYB301 benign simulator"

BEACON_DELAY = 3


# Below is the lab behaviour

print("[+] CYB301 benign simulator starting")

sandbox = Path.home() / "cyb301_sandbox"

sandbox.mkdir(exist_ok=True)

marker = sandbox / MARKER_FILENAME

marker.write_text(
	f"{TEST_MESSAGE}\n"
	f"Student: {STUDENT_TAG}\n"
	f"Host:	{socket.gethostname()}\n"
	f"OS: {platform.system()}\n"
)

print(f"[+] Created marker file: {marker}")

data = {
	"student": STUDENT_TAG,
	"host": socket.gethostname(),
	"os": platform.system(),
	"message": TEST_MESSAGE
}

query = urllib.parse.urlencode(data)

url = LAB_SERVER + "/?" + query

print(f"[+] Waiting {BEACON_DELAY} seconds")

time.sleep(BEACON_DELAY)

print("[+] Sending benign HTTP beacon")
print(f"[DEBUG] URL = {url}")

try:
	with urllib.request.urlopen(url, timeout=5) as response:
		print(f"[+] Server responded: HTTP {response.status}")
except Exception as error:
	print(f"[-] Connection failed: {error}")

print("[+] Simulator Finished")
