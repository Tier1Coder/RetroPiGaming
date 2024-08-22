import serial.tools.list_ports
import pyautogui

ports = serial.tools.list_ports.comports()     
serialInst = serial.Serial()

portList = []

for port in ports:
    portList.append(str(port))
    print(str(port))

whatPort = input("Select Port: COM")

for x in range(len(portList)):
    if portList[x].startswith("COM" + str(whatPort)):
        portVariable = "COM" + str(whatPort)
        print(portVariable)

serialInst.baudrate = 9600
serialInst.port = portVariable
serialInst.open()

pyautogui.PAUSE = 0

keysDown = {}   

keyMap = ['D', 'W', 'space', 'A', 'E']


def keyDown(key):
    if key not in keysDown:
        keysDown[key] = True
        pyautogui.keyDown(key)
        #  print('Down: ', key)

def keyUp(key):
    if key in keysDown:
        del(keysDown[key])
        pyautogui.keyUp(key)
        #  print('Up: ', key)

def handleJoyStickAsArrowKeys(x, y):
    if x > 0:
        keyDown('right')
        keyUp('left')
    elif x < 0:
        keyDown('left')
        keyUp('right')
    else:
        keyUp('left')
        keyUp('right')

    if y > 0:
        keyDown('down')
        keyUp('up')
    elif y < 0:
        keyDown('up')
        keyUp('down')
    else:
        keyUp('up')
        keyUp('down')

buttonState = 0


def handleButtonState(state):
    for i in range(5):
        if not keyMap[i]:
            continue

        if buttonState >> i & 1:
            keyDown(keyMap[i])
        else:
            keyUp(keyMap[i])

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        temporary = packet.decode("utf")
        values = temporary.split(",")
        if len(values) >= 3:
            dx = int(values[0])
            if abs(dx) < 10:
                dx = 0
            dy = int(values[1])
            if abs(dy) < 10:
                dy = 0
            buttonState = int(values[2])
            handleJoyStickAsArrowKeys(dx, dy * -1)
            handleButtonState(buttonState)








