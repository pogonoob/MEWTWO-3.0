# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/ae5a7b751569bb8b5062e.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "HELLO THIS IS Mewtwo 3.0 \n\n"
  LEGENDX += "ALL SYSTEM ARE WORKING PROPERLY\n\n"
  LEGENDX += "Mewtwo 3.0 OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {swami} ☺️\n\n"
  LEGENDX += "FULLY UPDATED\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADDING ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/LEGENDX22"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOYX🔥
  PROBOYX = [[Button.url("REPO-Mewtwo3.0", "https://github.com/pogonoob/MEWTWO-3.0"), Button.url("REPO-Mewtwo", "https://github.com/op-coder482/Soul-thunder-")]]
  PROBOYX +=[[Button.url("DEPLOY-Mewtwo3.0", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fpogonoo%2FMEWTWO-3.0&template=https%3A%2F%2Fgithub.com%2Fpogonoob%2FMEWTWO-3.0P%2FLE"), Button.url("DEPLOY-Mewtwo", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fop-coder482%2FSoul-thunder-&template=https%3A%2F%2Fgithub.com%2Fop-coder482%2FSoul-thunder-")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot")
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/mewtwo1_botsupport"), Button.url("SUPPORT GROUP", "https://mewtwo1_botsupport")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="Swami")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=swami)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 and PROBOYX 🔥
  LEGENDX = "HELLO THIS IS MEWTWO 3.0 \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "Mewtwo 3.0 OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {swami} ☺️\n\n"
  LEGENDX += "FULLY UPDATED BOT\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADDING ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/Swami_2_0_0_5"), Button.url("DEVLOPER", "https://t.me/Swami_2_0_0_5")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF GRAND OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/LEGENDXOP/LEGEND-X")]])
# PROBOYX 🔥 LEGENDX22

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
