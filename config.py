from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 7291869416
bot_user = "matrixt25bot"
api_id = 17104807
api_hash = "082b437fa75ed409a45b8660b95a97c0"
session = "BAAP7J-6KIHas3GI0PHLxBmcHk5XbmRvEC_PRRd8H5kBIa-PoN2CxbeD9CvCF0VlsvnEHuZQ9sy_y3_KzZE8qP8aZAYV8Orehnpdv79wnAopxLusdRHTjH3wCINFMdGirU7oQCuyaRoc_V1RoUxOhnMYdNBazaOGi7G4B4gbthT_IfPa5Q_-dOc0RuaKuXFsXathQ1eelcCbV5SxANgL3uuAFwa-yMFWdTii197jWxFQmv_NjWwz9-LqaXiNnkhftqTXJwpXLj0-eKBFqfgmdrKG0YR3CcuuHc-9wAlJVxGeaYqMZqZXe69eVmm1NQl3wk7tidonHfTMqnDL1bgv0HkPAAAAAEGIcKsA"
token = "6795500397:AAF2iJw25Fdx-2QXGnkP_zj8PUZ8Rl8gYjA"
sudo_command = [7291869416, 7291869416]
pm = "-1002059513294"
mention = "-1002059513294"
plugins = dict(root="plugins")
app = Client("user:Amrsabrrybot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Amrsabrrybot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
