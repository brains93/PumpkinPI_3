from inky.auto import auto
inky_display = auto()
inky_display.set_border(inky_display.WHITE)
from PIL import Image, ImageFont, ImageDraw

img = Image.open("/home/pi/pumpkinpiactive.png")
inky_display.set_image(img)
inky_display.show()
