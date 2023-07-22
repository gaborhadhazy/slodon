# https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L35-L56

__all__ = [
    "KEYEVENTF_KEYDOWN",
    "KEYEVENTF_KEYUP",
    "LEFT",
    "RIGHT",
    "MIDDLE",
    "MOUSEEVENTF_LEFTDOWN",
    "MOUSEEVENTF_MIDDLEDOWN",
    "MOUSEEVENTF_RIGHTDOWN",
    "MOUSEEVENTF_LEFTUP",
    "MOUSEEVENTF_RIGHTUP",
    "MOUSEEVENTF_MIDDLEUP",
    "MOUSEEVENTF_LEFTCLICK",
    "MOUSEEVENTF_RIGHTCLICK",
    "MOUSEEVENTF_MIDDLECLICK",
    "PRIMARY",
    "FAILSAFE_POINTS",
    "MINIMUM_DURATION",
    "MINIMUM_SLEEP",
    "MOUSEEVENTF_WHEEL"
]

KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

# Constants for the mouse button names:
LEFT = "left"
MIDDLE = "middle"
RIGHT = "right"
PRIMARY = "primary"
SECONDARY = "secondary"

MINIMUM_DURATION = 0.1  # 100 ms
MINIMUM_SLEEP = 0.05  # 50 ms

# Event codes to be passed to the mouse_event() win32 function.
# Documented here: http://msdn.microsoft.com/en-us/library/windows/desktop/ms646273(v=vs.85).aspx
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_LEFTCLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_RIGHTCLICK = MOUSEEVENTF_RIGHTDOWN + MOUSEEVENTF_RIGHTUP
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_MIDDLECLICK = MOUSEEVENTF_MIDDLEDOWN + MOUSEEVENTF_MIDDLEUP
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_HWHEEL = 0x01000


FAILSAFE_POINTS = [(0, 0)]  # https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L573C27-L573C27
