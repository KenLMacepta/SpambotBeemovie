import pyautogui, time
tiempo = 5 #tiempo de espera antes de iniciar el programa
f = open('beemovie.txt', 'r')
time.sleep(tiempo)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

