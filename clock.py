import time
import sys

def hide_cursor():
	sys.stdout.write("\033[?25l")
	sys.stdout.flush()

def stop_watch():
    m = 0
    while True:
        time.sleep(1)
        s = 0
        curr_time = str(f"{m:02d}") + ":" + str(f"{s:02d}")
        print(curr_time)
        for _ in range(59):
            time.sleep(1)
            s += 1
            curr_time = str(f"{m:02d}") + ":" + str(f"{s:02d}")
            print(curr_time)
        m += 1


def keep_time(hour, minute, am_pm):
    m = minute
    h = hour
    am = "A.M"
    pm = "P.M"
    if am_pm == "A.M":
    	current = am
    elif am_pm == "P.M":
    	current = pm
    else:
    	return
    while True:
        time.sleep(1)
        s = 0
        curr_time = f"{h}:{m:02d}:{s:02d} {current}"
        print(curr_time, end="\r")
        for _ in range(59):
            time.sleep(1)
            s += 1
            curr_time = f"{h}:{m:02d}:{s:02d} {current}"
            print(curr_time, end="\r")
        m += 1
        if m == 60:
            h += 1
            m = 0
            if h == 12:
            	if current == "A.M":
            		current = pm
            	else:
            		current = am
            if h == 13:
            	h = 1

hide_cursor()
keep_time(12, 59, "P.M")
