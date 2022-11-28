import pyautogui as pag
import time

print('O programa iniciará em 5 segundos')
time.sleep(5)

for i in range(1000):
    pag.write('Eu te amo')
    time.sleep(0.2)
    pag.press('Enter')