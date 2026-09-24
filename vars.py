

from os import environ

API_ID = int(environ.get("API_ID", "32718784"))
API_HASH = environ.get("API_HASH", "e0eba9c10096bd62c5fc165790983c83")
BOT_TOKEN = environ.get("BOT_TOKEN", "8961265693:AAE_Z1YyxpTXkXuSxLNCE5i2DXqSVWMCQVQ")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





