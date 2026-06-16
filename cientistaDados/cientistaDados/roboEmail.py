import pyautogui
import pyperclip
import webbrowser
import time

email = 'brenda.andrade@edu.senai.br'
assunto = 'Relatório mensal de faturamento'

webbrowser.open('mail.google.com')
time.sleep (8)
pyautogui.click(x=145, y=172)
time.sleep (8)
pyperclip.copy(email)
pyautogui.hotkey('ctrl','v')
time.sleep (3)
pyautogui.press('enter')
pyautogui.press('tab')
time.sleep (3)
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyautogui.press('tab')

corpoEmail = """
Relatório do faturamento de Dezembro

Att
Brenda Andrade
"""

pyperclip.copy(corpoEmail)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
pyautogui.press('enter')