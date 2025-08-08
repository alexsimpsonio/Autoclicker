import pyautogui
import time

time.sleep(5)  # Pause for 5 seconds
x, y = pyautogui.position()  # Get current mouse position
print(f"Mouse coordinates: ({x}, {y})")
