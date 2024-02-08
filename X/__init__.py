from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("ᴡᴀʀɴɪɴɢ: ᴀᴘɪ ɪᴅ ɴᴏᴛ ꜰᴏᴜɴᴅ ᴜꜱɪɴɢ 𝐉𝐚𝐩𝐚𝐧𝐞𝐬𝐞 𝐗 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ᴀᴘɪ ⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("ᴡᴀʀɴɪɴɢ: ᴀᴘɪ ʜᴀꜱʜ ɴᴏᴛ ꜰᴏᴜɴᴅ ᴜꜱɪɴɢ 𝐉𝐚𝐩𝐚𝐧𝐞𝐬𝐞 𝐗 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ᴀᴘɪ ⚡")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("ᴡᴀʀɴɪɴɢ: ʙᴏᴛ ᴛᴏᴋᴇɴ ɴᴏᴛ ꜰᴏᴜɴᴅ ᴘʟᴢ ᴀᴅᴅ ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="X/modules/bot"),
    in_memory=True,
)

if STRING_SESSION1:
   print("ᴄʟɪᴇɴᴛ1: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="X/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("ᴄʟɪᴇɴᴛ2: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="X/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("ᴄʟɪᴇɴᴛ3: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="X/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("ᴄʟɪᴇɴᴛ4: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="X/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("ᴄʟɪᴇɴᴛ5: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="X/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("ᴄʟɪᴇɴᴛ6: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="X/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("ᴄʟɪᴇɴᴛ7: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="X/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("ᴄʟɪᴇɴᴛ8: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="X/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("ᴄʟɪᴇɴᴛ9: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="X/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("ᴄʟɪᴇɴᴛ10: ꜰᴏᴜɴᴅ.. ꜱᴛᴀʀᴛɪɴɢ.. ✨")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="X/modules")) 
   clients.append(client10)
