import asyncio
import importlib
from pyrogram import Client, idle
from X.helper import join
from X.modules import ALL_MODULES
from X import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: ʙᴏᴛ ᴛᴏᴋᴇɴ ꜰᴏᴜɴᴅ ʙᴏᴏᴛɪɴɢ ʙᴏᴛ..")
    for all_module in ALL_MODULES:
        importlib.import_module("X.modules" + all_module)
        print(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ {all_module} ✨")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"ꜱᴛᴀʀᴛᴇᴅ {ex.first_name} 💫")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
