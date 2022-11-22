from instabot import Bot
from create_quote import generateQuotedImage
import os

# login credentials
MY_USERNAME = os.environ["WISEBOT_INSTA_USERNAME"]
MY_PASSWORD = os.environ["WISEBOT_INSTA_PASSWORD"]

# created bot & logged it in
bot = Bot()
bot.login(username=MY_USERNAME, password=MY_PASSWORD)


# generating new post
quote = generateQuotedImage()
img = "generated_imgs/quote_img.jpg"

bot.upload_photo(img, caption=f'''"{quote[0]}"
                            
                            ~{quote[1]}
                            
                            
                            
                            #wisebot89''')
