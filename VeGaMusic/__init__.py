from VeGaMusic.core.bot import Zoro
from VeGaMusic.core.dir import dirr
from VeGaMusic.core.git import git
from VeGaMusic.core.userbot import Userbot
from VeGaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zoro()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
