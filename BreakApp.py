import webbrowser
import time

times = 0
print ("Working day started at" + time.ctime())
while times < 4:
    time.sleep(10) #open the browser every 10 sec.
    webbrowser.open_new("https://www.youtube.com/watch?v=thIVtEOtlWM")
    times += 1
