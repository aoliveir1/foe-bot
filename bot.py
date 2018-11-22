import time
import pyautogui
from pyvirtualdisplay import Display

with Display():
  time.sleep(1)
  pyautogui.moveTo(0, 0)
  time.sleep(1)
  pyautogui.moveTo(200, 200)
