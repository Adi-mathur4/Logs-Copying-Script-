from sys import prefix, setprofile
import time 
import os
import pyautogui
import socket 
pyautogui.FAILSAFE = False

#Paths and IP for the flow of data
SUT_Name = (socket.gethostname()) 
directory_file = r'File Name'
remote_connection_ip = "IP of the Server"
remote_connection_directory_address = r'File Locatipon '
xml_address = r'netsh wlan add profile filename=".xml file for the wifi" interface="Wi-Fi"'
Server_Username  = 'User name of the server'
Server_Password = 'password of the server'

Config = int(pyautogui.prompt("Directory Details"))
if Config==1 or Config==2 or Config==3:
    KPI = int(pyautogui.prompt("Inner Directory Details"))
    if Config==1 and KPI==1:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    elif Config==1 and KPI==2:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    elif Config==1 and KPI==3:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    elif Config==1 and KPI==4:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    elif Config==1 and KPI==5:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    elif Config==2 and KPI==1:
        robocopy_address = r'"Directory Path" /e /Z /sec /mov'
    else:
        pyautogui.alert('Incorrect Selection!!')
        exit()
elif Config==4:
    robocopy_address = r'"Directory Path" /e /Z /sec /mov'
else:
    pyautogui.alert('Incorrect Selection. Exiting Log Copying System')
    exit()



def install_7zip():
    os.system('start cmd \c')
    pyautogui.sleep(2)
    pyautogui.typewrite(r'cd C:\Users\%username%\Desktop\Robocopy',interval=0.02)
    pyautogui.sleep(1)
    pyautogui.press('enter')  
    pyautogui.sleep(1)

    pyautogui.typewrite(r'choco install "%userprofile%\Desktop\Robocopy\7zip.install.18.6.nupkg" -yes')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)

    pyautogui.typewrite('exit')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)


def WiFi_Connect():
    os.system('start cmd \k')
    time.sleep(1)

    pyautogui.typewrite(xml_address,interval=0.01)
    time.sleep(2)
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.typewrite('netsh wlan connect name=DPMOLogStore',interval=0.01)
    pyautogui.press('enter')
    time.sleep(4)

    pyautogui.typewrite('exit')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def zip_file():

    os.system('start cmd \k')
    pyautogui.sleep(1)
    pyautogui.typewrite('cd "C:\Program Files"')
    pyautogui.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite('cd ')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.typewrite(r'7z a C:\Users\%username%\Desktop\Robocopy\Logs\Reports_'+SUT_Name+'.zip '+'"File Name'+SUT_Name+'"')
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.typewrite('exit')
    pyautogui.sleep(1)
    pyautogui.press('enter')

def Renaming_Folder():
    os.system('start cmd \k')
    pyautogui.sleep(1)
    pyautogui.typewrite(r'cd File Directory')
    pyautogui.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite('ren Reports Reports_'+SUT_Name)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite('exit')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def Copy():
    os.system('start cmd \k')
    time.sleep(2)
    pyautogui.typewrite(r'cd C:\Users\%username%\Desktop\Robocopy')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    
    pyautogui.typewrite(r'net use \\IP /user:'+Server_Username+' '+Server_Password)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.typewrite(robocopy_address)
    time.sleep(1)
    pyautogui.press('enter')



install_7zip()
WiFi_Connect()
Renaming_Folder()
zip_file()
Copy()



