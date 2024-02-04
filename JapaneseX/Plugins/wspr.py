# COPYRIGHT 2024-25 BY Nobitaa_xd
"""
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
             DONT DARE TO KANG WITHOUT CREDITS
"""
# IF YOU KANG THEN KEEP CREDITS PLEASE 🥺
from telethon import events, Button
import re, os
from JapaneseX import id
from JapaneseX import xbot
@xbot.on(events.InlineQuery(pattern='wspr'))
async def inline_proboy(event):
  REDMOON = event.text[5:]
  REDMOON, RAYEN = RAYEN.split('@')
  os.system("rm -rf wspr.txt")
  f = open("wspr.txt", "a")
  f.write(RAYEN + "\n" + REDMOON)
  f.close()
  NOBITA_XD = event.builder
  RAYEN = [[Button.inline("🔐 Sʜᴏᴡ", data='secret')]]
  RAYEN += [[Button.switch_inline("Rᴇᴘʟʏ", query="wspr", same_peer=True)]]
  ALAIN = NOBITA_XD.article(title=f"Wʜɪsᴘᴇʀ Fᴏʀ @{RAYEN}", text=f"<b>📩 Sᴇᴄʀᴇᴛ Msɢ</b> Tᴏ <b>(RAYEN}</b>. Oɴʟʏ Hᴇ/Sʜᴇ Cᴀɴ Oᴘᴇɴ Iᴛ..", buttons=REDMOON, parse_mode="html")
  await event.answer([ALAIN])

@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b'secret')))
async def wspr(event):
  try:
    f = open("wspr.txt")
    NOBITA_XD = f.readlines()[0]
    f.close()
    pro = open("wspr.txt")
    RAYEN = pro.readlines()[1].lower()
    pro.close()
    bot = await xbot.get_me()
    sender = f"{event.sender.username}".lower()
    me = f"{borg.me.username}".lower()
    if sender == REDMOON or sender == me or event.sender_id == id:
       await event.answer(NOBITA_XD, alert=True)
    else:
       await event.answer("Yes You, Little Shit, Why're u seeing my msg??", alert=False)
  except:
    await event.answer(f"Use @{bot.username} wspr <msg> <@ sender username>\n\nAnd ofc, remove those <>", alert=True)
