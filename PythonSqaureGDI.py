from win32gui import *
from win32api import *
from win32ui import *
from win32con import *


desk = GetDC(0)
x = 100
y = 100
x_2 = 100
y_2 = 100


for i in range(5):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10
