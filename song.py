# Copyright (C) 2024 By Japanese X Userbot 

# ~ NOBITA_XD

# Reserved, Copyrighted by Japanes X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by Japanese X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by Japanese X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar  

# Last Warn - Undo the removed part else be ready for DMCA by NOBITA_XD
# Mobile me back option he uspe click karde kang kiya to dekh


import os, re
from JapaneseX Userbot  import id, ID, devs
from telethon.tl.functions.contacts import BlockRequest as block
from telethon import Button, custom, events, functions

# back button click kr 
from JapaneseX Userbot  import NAME
JAPANESEUSERBOT_USER = NAME

BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
  BOT_MAD = f"Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ נαραηεsε x υsεявσт, ғᴏʀ {JAPANESEUSERBOT_USER}'s Pʀᴏᴛᴇᴄᴛɪᴏɴ "
else:
  BOT_MAD = BOT_MSG   

WARN = (
  f'''
{BOT_MAD}
Hᴇʏ ᴛʜᴇʀᴇ!! I'ᴍ נαραηεsε x υsεявσт ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ {JAPANESEUSERBOT_USER}..\nDᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈**
Mʏ Mᴀsᴛᴇʀ {JAPANESEUSERBOT_USER}  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !! \n"
Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..
Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...
Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ..
Cʜᴏᴏsᴇ ᴀɴʏ Rᴇᴀsᴏɴ & GTFO
''')

JAPANESEUSERBOT_BOT_PIC = os.environ.get("PMPERMIT_PIC", None)
if JAPANESEUSERBOT_BOT_PIC is None:
    JAPANESEUSERBOT_PIC = "https://mallucampaign.in/images/img_1706864199.jpg"
else:
    JAPANESEUSERBOT_PIC = JAPANESEUSERBOT__BOT_PIC

back = [[Button.inline("«« Bᴀᴄᴋ", data="pm_back")]]
@xbot.on(events.InlineQuery())
async def inline_nobitaaxd(event):
  piro = event.text
  if event.sender_id == bot.me.id and piro == 'pmsecurity' or event.sender_id==id and piro=='pmpermit':
    NOBITA_XD= event.builder
    NOBITA_XD = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='hmmmmm')]]
    NOBITA_XD+= [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
    NOBITA_XD = NOBITA_XD.photo(file=JAPANESEUSERBOT_PIC, text=WARN, buttons=NOBITA_XD)
    await event.answer([NOBITA_XD])
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'chutia')))
async def chutia_aayaa(event):
  global back
  if event.sender_id !=bot.me.id or event.sender_id != id:
     CONFIRM = [[Button.inline("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", data='confirm_chutia')]]
     CONFIRM += back
     await event.edit("Aʀᴇ ʏᴏᴜ sᴘᴀᴍᴍᴇʀ?", buttons=CONFIRM)
  else:
     No = "Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'confirm_chutia')))
async def confirmed(event):
  pro=event.sender_id
  global block
  if pro != bot.me.id or pro != ID:
    await event.edit("Oʜᴋ sᴏ ɢᴏ ᴛᴏ ʜᴇʟʟ ᴅᴜᴅᴇ 😁")
    await bot(block(pro))
  else:
     No = "Nᴏ ᴍᴀsᴛᴇʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴘᴀᴍᴍᴇʀ"
     await event.answer(No, alert=False)

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'frnd_bsdk')))
async def Inline_nobitaaxd(event):
  piro = event.sender_id
  global back
  if piro != bot.me.id or piro != id:
    await event.edit("Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!", buttons=back)
  else:
    await event.answer("Mᴀsᴛᴇʀ, ᴜsᴇ .approve ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʜɪᴍ")
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'noobda')))
async def noobda (event):
  global back
  Piro = [[Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/Japanese_Userbot_Chat "), Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/Japanese_Userbot")]]
  Piro += [[Button.url("Rᴇᴘᴏ", "https://github.com/Japanese-Userbot/Japanese-X-Userbot")]]
  Piro += back
  await event.edit("Cʜᴇᴄᴋɪɴɢ ᴛʜᴇsᴇ ʟɪɴᴋs", buttons=Piro)
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'pm_back')))
async def inline_nobitaaxd(event):
  acha = event.sender.first_name
  jnl = bot.me.first_name
  NOBITA_XD = [[Button.inline("Fʀɪᴇɴᴅ", data='frnd_bsdk'),Button.inline("Sᴘᴀᴍ", data='chutia')]]
  NOBITA_XD += [[Button.inline("Wᴜᴛ's ᴛʜɪs ?",data='noobda')]]
  await event.edit(f"Hᴇʟʟᴏ {acha}, ᴍʏ sᴇʟғ נαραηεsε x υsεявσт , ʜᴇʀᴇ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ {jnl}!", buttons=NOBITA_XD)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'nino')))
async def _(event):
  global back
  await event.edit("Oᴋɪᴇ ᴡᴇɪᴛ ᴛɪʟʟ ᴍʏ ᴍᴀsᴛᴇʀ ʀᴇᴘʟʏ ʏᴏᴜ, Hᴇ ᴡɪʟʟ ʀᴇᴘʟʏ ʏᴏᴜ sᴏᴏɴ ᴀsᴀᴘ !!", buttons=back)
  
@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'hmmmmm')))
async def _(event):
  kk = [[Button.inline("Yᴇs", data='confirm_chutia')]]
  kk += [[Button.inline("Nᴏ", data='nino')]]
  await event.edit("Wɪʟʟ ʏᴏᴜ sᴘᴀᴍ?", buttons=kk)

  
 # Copyright (C) 2024 By Japanese X Userbot 

# ~ NOBITA_XD

# Reserved, Copyrighted by Japanes X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by Japanese X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Reserved, Copyrighted by Japanese X Userbot , only for Japanese X Userbot  If found in any other repo, be ready for DMCA

# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# back click kar  

# Last Warn - Undo the removed part else be ready for DMCA by NOBITA_XD
# Mobile me back option he uspe click karde kang kiya to dekh
