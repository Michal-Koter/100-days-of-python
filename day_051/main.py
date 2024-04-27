import os

from day_051.internet_speed_x_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 300
PROMISED_UP = 50
CHROME_DRIVER_PATH = "/Users/koter/Downloads/chromedriver"
X_EMAIL = os.environ.get("EMAIL")
X_PASSWORD = os.environ.get("PASSWORD")

bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
bot.get_internet_speed()
bot.tweet_at_provider(X_EMAIL, X_PASSWORD)
