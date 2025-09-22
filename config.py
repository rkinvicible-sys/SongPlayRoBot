import os
API_ID = int(os.getenv("20666532"))
API_HASH = os.getenv("da5811243de26f755bb80615e34689db")
BOT_TOKEN = os.getenv("8283865282:AAGS4C4bdTAu7mJo-wOLuBTbQCMoXDU9guo")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
