#needs python-xlib
#run this as a background app 
#and shift focus to e.g. Okular showing a pdf in Presentation mode
#first a left click event is sent ( move to next page)
#then a right click event is sent ( move to previous page)
#
#-----
#First step towards gesture controlled slideshows

import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.error
import Xlib.ext.xtest
import time

display = Xlib.display.Display()
def mouse_click(button): #button= 1 left, 2 middle, 3 right
    Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonPress, button)
    display.sync()
    Xlib.ext.xtest.fake_input(display,Xlib.X.ButtonRelease, button)
    display.sync()

time.sleep(10)
mouse_click(1)
time.sleep(3)
mouse_click(3)
