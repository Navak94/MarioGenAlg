from pywinauto.keyboard import send_keys, KeySequenceError

send_keys('some text{ENTER 2}some more textt{BACKSPACE}', with_spaces=True)
