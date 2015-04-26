import sys
sys.path.insert(0, './lib/pyxhook')
import time
import pyxhook


def printevent(self, event):
    print event

# create a hook manager
hm = pyxhook.HookManager()
hm.HookMouse()
# watch for all mouse events
hm.MouseAllButtonsDown = hm.printevent
hm.MouseAllButtonsUp = hm.printevent
# set the hook
hm.start()
