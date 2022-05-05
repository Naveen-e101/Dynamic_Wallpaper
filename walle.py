import ctypes
from PIL import Image,ImageDraw,ImageFont
import datetime
import json
import platform

data = datetime.datetime.now()

date = str(data.date())
with open("C:\\No_touching\\sample.json", "r") as openfile:
    json_obj = json.load(openfile)

if(date == json_obj["date"]):
    print("Exit")
    exit()

json_obj["date"] = date

json_obj["day"] = json_obj["day"] + 1
day = json_obj["day"]

SIZE = (1920,1080)
font_size = 100
img = Image.new("RGB",SIZE)
msg = "Status \nPlatform: " + platform.system() + "\nDay: " + str(day)

font = ImageFont.truetype(font="C:\\No_touching\\mono.otf",size=font_size)
draw = ImageDraw.Draw(img)

w,h = font.getsize_multiline(msg)
anc = ((SIZE[0]-w)/2,(SIZE[1]-h)/2)
draw.multiline_text(anc, msg, fill=(255,255,255), align="center",font=font,)

img.save("Rip.png")
with open("C:\\No_touching\\sample.json", "w") as openfile:
    json.dump(json_obj, openfile)

WALLPAPER_PATH = "C:\\No_touching\\Rip.png"
sys_info = ctypes.windll.user32.SystemParametersInfoW

sys_info(20,0,WALLPAPER_PATH,3)