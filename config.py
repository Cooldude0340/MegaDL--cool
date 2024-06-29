# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 2712818))
    API_HASH = os.environ.get("API_HASH", "fda406cc4f648c303a0fb77255f2a026")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1880774062:AAHbe7FpEsd1UT5Yx7PITGrSTuWmQfQWc_g")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1517181772))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 1713544941))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

🧑‍💻 **Developer:** [NoOne](https://t.me/shinchan_movies_hindi)

👥 **Support Group:** [Nope](https://t.me/shinchan_movies_hindi)

📢 **Updates Channel:** [shinchan movies](https://t. me/shinchan_movies_hindi)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
