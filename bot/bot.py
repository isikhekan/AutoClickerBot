import pyautogui
import cv2
import pyscreeze
import numpy as np

button_images = ['s1.png','s2.png','s3.png','s4.png','s5.png','s6.png','s7.png','s8.png','s9.png','s10.png','s11.png','s12.png','Screenshot_1.png','Screenshot_2.png','Screenshot_3.png','Screenshot_4.png','Screenshot_5.png','Screenshot_6.png','Screenshot_7.png']##,'ral.png','ral2.png','ral3.png','ral4.png',
## = ['cheatsheet2.png', 'cheatsheet3.png', 'cheatsheet4.png', 'cheatsheet5.png','cheatsheet6.png',
                 ##'cheatsheet7.png','cheatsheet8.png','cheatsheet9.png','cheatsheet10.png']
button_templates = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in button_images]

screen_width, screen_height = pyautogui.size()


def find_button():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    for button_template in button_templates:
        result = cv2.matchTemplate(screenshot, button_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.75
        if max_val >= threshold:
            return max_loc, button_template.shape

    return None, None


def click_button(location, shape):
    x, y = location
    button_height, button_width = shape
    pyautogui.PAUSE = 0
    pyautogui.click(x + button_width // 2, y + button_height // 2)


while True:
    button_location, shape = find_button()
    if button_location:
        click_button(button_location, shape)
