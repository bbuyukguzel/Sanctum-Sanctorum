__author__ = 'Batuhan BUYUKGUZEL'
import time
import datetime

command = ""
comp = []


def timer(minute, second):
        for m in range(minute, -1, -1):
            for s in range(second, -1, -1):
                print(str(m).zfill(2)+":"+str(s).zfill(2), end="\r")
                time.sleep(1)
        else:
            now = datetime.datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M"))
            comp.append(now)
            print("Time is up!")

def help():
    print("SPACE   Start or Stop the timer")
    print("-p  Pomodoro")
    print("-s  Short Break")
    print("-l  Long Break")
    print("-r  Reset Timer")
    print("-ss Print asdasd")


print("To list all available commands, enter -help.")
while True:
    command = input("pm@timer:~$ ").lower()
    if command == "-help":
        help()
    elif command == "-p":
        timer(24, 59)
    elif command == "-s":
        timer(4, 59)
    elif command == "-l":
        timer(9, 59)
    elif command == "-ss":
        print(comp.strftime("%Y-%m-%d %H:%M"))
    else:
        print("Wrong Command!")






