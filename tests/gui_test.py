import pyscreenshot as ImageGrab

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()
