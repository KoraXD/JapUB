import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "X"])

async def join(client):
    try:
        await client.join_chat("Japanese_Userbot")
    except BaseException:
        pass
