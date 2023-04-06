#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6039043446:AAHf8ODju2FpNFBXj7v2-MwC0HxpLAu_0wU")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ":28394784"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", ":9544a3ad7d8660acbae0dcf553c808e5")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQGxRSAACtT62Vgw4WrpSTTksGRAeN5SNJz6k8gtsti5lgMfACzQ84_2jRozB95aBKyAoTOMgfCUuQCKSz-frS4AJB24M1ADfPUGpimbY7fcNzweu8kE4lTGIegVq5i-meTAPO02x7eeCEH0fOlX3VYH8yjv0OXc6i1UzCiLzGqnajTdpamMTiOt4Goel84FYrArsE1J0rbE7FXMVhJLLS0jM_mLKHCfxPPqJ8nUeuDYLTc_A9YKS6lLDHiMRHW9mh3m2DlN_0TwtqoYogZ0wynqimdt90pmBxgXDIvl8fU8YzZrplTEL59v_od7N1-Sz2yxK1kQqxERfRA9gtAwegweXlOwrgAAAABF5vF9AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://forward:forward@cluster1.pgynkyr.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
