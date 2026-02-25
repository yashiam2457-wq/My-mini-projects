from PIL import *
import time
import pyscreenshot
def shot():
    time.sleep(5)
    image=pyscreenshot.grab()
    image.show()
    image.save("screenshot1.png")