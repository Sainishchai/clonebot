import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "6172813223:AAHnrXvZc57jvKvbSpM1bwnHl8V8kHddRzk"
    APP_ID = 28394784
    API_HASH = "9544a3ad7d8660acbae0dcf553c808e5"
    TG_USER_SESSION = "BQGxRSAAeWqibGHhOO0vjkM5dNc6NAabU7gaPxZDFUs0x1Qa39N4mdHfKG5QCPfo7zLH_M-xxZaJxLCO26_KD4ALRTvt_klxrVBeg_BsjSUxN9DituLxeoQY2Se0AnT4-bpLZu_4YbHQsT7NMoHWQm9krYPLTmXXVwTFaB36tnFnRhbPnuzmrcLBTyGvym8KDU6zCKsSvd1yqEDEGD0dW__IcJ2KXprotyZDmFHpOs-Ag8XlnryaIZONh5PTOJUtAD_XXKv_yTXTnl0QRsJyx2F0Gy4B4DStae83FoGEcKh7UVL4KUmzpnuve9x3yqeLhMuCFzNPUfIyyVxaL76Ex1BB8CPnCwAAAABF5vF9AA"
    DB_URI = "mongodb+srv://forward:forward@cluster1.pgynkyr.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
