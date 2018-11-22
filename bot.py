import time
from pymouse import PyMouse

mouse = PyMouse()
mouse.move(0,0)
time.sleep(1)
mouse.move(100,100)
