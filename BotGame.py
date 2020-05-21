# Chrome dino bot(automatically runs) program
from PIL import ImageGrab
import pyautogui
from time import sleep
class Cordinates():
    replayBtn = (799,386)
    dinasaur = (562,400)
    
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    
restartGame()

def pressSpace():
    pyautogui.keyDown('space')
    sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
    
restartGame()
sleep(1)
pressSpace()
