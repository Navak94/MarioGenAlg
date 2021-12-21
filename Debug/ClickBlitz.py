from pynput.mouse import Button, Controller

mouse = Controller()

#mouse.click(Button.left, 2)

for x in range (0,10000):
   mouse.position = (1280, 1049)
   mouse.click(Button.left, 1)
   mouse.position = (1291, 1006)
   mouse.click(Button.left, 1)
   
