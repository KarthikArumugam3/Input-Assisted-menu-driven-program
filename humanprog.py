import os
import time


localtime = time.asctime(time.localtime(time.time()))



while True:
    print("\n")
    print("****************************************")
    print("WELCOME I AM YOUR PERSONAL APP ASSISTANT",)
    print("****************************************")
    print("Today is",localtime,end="")
    print("\n")
    print("What can i do for you?",end="")
    print("\n")
    print("Here are some things that you can do \n\nTry Writing:- \n----------- \nHey can you open an Ide for me? \nPlease launch text editor \nexecute atom ")
    print("\n")
    p = input() 

    if (("run" in p) or ("execute") or ("launch" in p) or ("open" in p))and (("chrome" in p) or ("browser" in p)):
        os.system("chrome")
    elif (("run" in p) or ("execute") or ("launch" in p) or ("open" in p) )and (("editor" in p) or ("notepad" in p)):
        os.system("notepad")
    elif (("run" in p) or ("execute") or ("launch" in p) or ("open" in p))and (("mediaplayer" in p) or ("windowsplayer" in p)):
        os.system("wmplayer")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("brackets" in p):
        os.system("brackets")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("atom" in p):
        os.system("atom")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("ide" in p) or ("pycharm" in p)):
        os.system("PyCharm")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("files" in p):
        os.system("explorer")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("calculator" in p):
        os.system("calc")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("paint" in p):
        os.system("mspaint")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("character map" in p) or ("charactermap" in p)):
        os.system("charmap")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("taskmanager" in p) or ("task manager" in p)):
        os.system("taskmgr")

    elif ("exit" in p) or ("quit" in p):
        break

    else:
        print("not supported")
